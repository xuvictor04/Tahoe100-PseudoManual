---
symbol: "MINDY3"
type: "gene"
col: 7288
ensembl_id: "ENSG00000148481"
name: "MINDY lysine 48 deubiquitinase 3"
location: "10p13"
module: 65
arm: "+"
pooled_cpm: 54.91
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# MINDY3

*MINDY lysine 48 deubiquitinase 3* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.82× (z +10.0, q 9e-21, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.586× (z -8.9, q 3e-16, down in 40 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.680× (z -6.4, q 2e-08, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALG9]] (+0.74, fdr 7e-06), [[ANAPC4]] (+0.74, fdr 7e-06), [[RTCA]] (+0.73, fdr 7e-06); moves opposite to [[THOC6]] (-0.66, fdr 1e-05), [[OPA3]] (-0.61, fdr 1e-05), [[PPP1R10]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7288.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.82×** | +10.0 | 9e-21 | 41/48 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.73×** | +9.2 | 1e-17 | 43/48 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +7.9 | 7e-13 | 37/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.25×** | +7.1 | 2e-10 | 33/49 (BT-474, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.33×** | +6.7 | 2e-09 | 31/48 (HOP62, RKO, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.29×** | +4.2 | 0.002 | 25/48 (SW480, H4, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.008 | 21/48 (SW48, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.012 | 23/48 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.036 | 17/48 (A-172, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +3.4 | 0.038 | 11/48 (BT-474, NCI-H2347, …) | top dose only |  |
| [[Tadalafil (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.041 | 15/48 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.3 | 0.043 | 14/48 (C32, AsPC-1, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.062 | 17/49 (PANC-1, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.071 | 14/49 (HepG2/C3A, C-33 A, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.20× | +3.0 | 0.091 | 10/48 (SW1417, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7288.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.586×** | -8.9 | 3e-16 | 40/48 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.583×** | -8.7 | 1e-15 | 27/41 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.680×** | -6.4 | 2e-08 | 33/48 (A-172, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.673×** | -6.1 | 1e-07 | 30/45 (RPMI-7951, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **0.732×** | -5.2 | 2e-05 | 28/47 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Thymol (drug)]] 5 µM |  | **0.826×** | -4.5 | 7e-04 | 21/48 (SNU-1, SW1417, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.782×** | -4.1 | 0.003 | 23/48 (NCI-H460, HOP62, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.799×** | -3.7 | 0.013 | 22/48 (HOP62, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.809×** | -3.5 | 0.026 | 19/48 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.811×** | -3.5 | 0.028 | 21/48 (HOP62, LoVo, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.813×** | -3.4 | 0.030 | 18/47 (HOP62, SW1417, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.830×** | -3.1 | 0.092 | 10/48 (PANC-1, SW 900, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.831×** | -3.1 | 0.092 | 11/49 (HS-578T, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7288. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 128 | 1 (1 ⚠) | 5 (4 ⚠) | [[Trametinib (drug)]] 5 µM 2.19× (z +8.7) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 5 µM 0.225× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.397× (z -10.0) |
| [[RKO (line)]] | wt | 74.9 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.83× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 40.1 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.37× (z +9.9) | [[Docetaxel (drug)]] 0.05 µM 0.418× (z -10.1) ⚠ transcription drop; cell-cycle shift, explains ~44% of this change |
| [[AN3 CA (line)]] | alt | 70.1 | 0 | 3 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.132× (z -10.7) |
| [[HOP62 (line)]] | alt | 32.5 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.276× (z -12.4) ⚠ cell-cycle shift, explains ~67% of this change |
| [[A-172 (line)]] | wt | 53.9 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.320× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 66.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -10.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 54.0 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.76× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.357× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 68.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -21.7) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 100 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -14.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 62.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -13.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 40.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -11.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 22.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.39× (z +9.3) | — |
| [[BT-474 (line)]] | alt | 58.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[COLO 205 (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -8.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 43.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0964× (z -13.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 63.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -9.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 29.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 32.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 34.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -9.7) ⚠ cell-cycle shift, explains ~66% of this change |
| [[SW480 (line)]] | alt | 60.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.448× (z -8.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 97.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 64.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7288), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG9]] | +0.74 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[ANAPC4]] | +0.74 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[RTCA]] | +0.73 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[MRS2]] | +0.73 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[LMBRD1]] | +0.72 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[JKAMP]] | +0.71 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[MED23]] | +0.71 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[ATP5F1C]] | +0.70 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[SKIC3]] | +0.70 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[METTL17]] | +0.70 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[ORC4]] | +0.70 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[VPS33B]] | +0.69 | +0.73 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC6]] | -0.66 | -0.68 / -0.53 | both halves | 1e-05 |  |
| [[OPA3]] | -0.61 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[PPP1R10]] | -0.61 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[DPH1-AS1]] | -0.60 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[PCF11]] | -0.60 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[SKIL]] | -0.59 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[SSUH2]] | -0.59 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[ERCC6L2]] | -0.59 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[PHF8]] | -0.59 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[RNF32-AS1]] | -0.58 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[SRCAP]] | -0.58 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[AKT1S1]] | -0.58 | -0.54 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.814). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-4.3, -10.5); signed map (-31.4, -12.5). **Vector** length 99.6, 25.9% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +5.9 | +6.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.7 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.3 | +3.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +3.9 | +4.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.8 | +7.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +3.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.3 | +0.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -5.7 | -3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.1 | -0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -5.1 | -4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -5.0 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -6.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -2.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -1.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | MINDY lysine 48 deubiquitinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:15,778,170-15,860,507 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13397, CARP, my042, DERP5; previously C10orf97, FAM188A |
| Gene groups (HGNC) | MINDY deubiquitinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H8M7](https://www.uniprot.org/uniprotkb/Q9H8M7) (Ubiquitin carboxyl-terminal hydrolase MINDY-3):

> Hydrolase that can remove 'Lys-48'-linked conjugated ubiquitin from proteins.

**Summary**, from NCBI Gene [80013](https://www.ncbi.nlm.nih.gov/gene/80013):

> The protein encoded by this gene contains a caspase-associated recruitment domain and may function in apoptosis. It has been identified as a tumor suppressor in lung and gastric cancers, and a polymorphism in the gene may be associated with gastric cancer risk. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:23578](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23578) · Entrez [80013](https://www.ncbi.nlm.nih.gov/gene/80013) · UniProt [Q9H8M7](https://www.uniprot.org/uniprotkb/Q9H8M7) · Ensembl [ENSG00000148481](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148481)

## Data

Gene col 7288: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7288); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7288, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7288]; `tensor/DDL_lfc|DDL_z.npy` [7288]; `embed/gene_vectors.npy` [7288]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7288 or target_col == 7288). Every well: [[MINDY3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MINDY3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
