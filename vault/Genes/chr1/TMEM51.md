---
symbol: "TMEM51"
type: "gene"
col: 10154
ensembl_id: "ENSG00000171729"
name: "transmembrane protein 51"
location: "1p36.21"
module: 154
arm: "+"
pooled_cpm: 77.67
n_lines_expressing: 46
n_dd_up: 0
n_dd_down: 25
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# TMEM51

*transmembrane protein 51* — 1p36.21

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (LoVo 2.13×, NCI-H460 3.08×, SW480 2.19×, Hs 766T 3.02×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (COLO 205 2.18×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.324× (z -33.5, q 0e+00, down in 41 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM51-AS1]] (+0.62, fdr 1e-05, ⚠ same locus), [[TNFRSF11A]] (+0.61, fdr 1e-05), [[UBTD1]] (+0.56, fdr 1e-05), [[CXCR4]] (+0.55, fdr 2e-05); moves opposite to [[IMPACT]] (-0.54, fdr 1e-05), [[N6AMT1]] (-0.53, fdr 3e-05), [[MAP2]] (-0.52, fdr 1e-05).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TMEM51-AS1]] → it (grade B ⚠); 3 go from it, the strongest it → [[CDS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (LoVo 2.13×, NCI-H460 3.08×, SW480 2.19×, Hs 766T 3.02×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (COLO 205 2.18×; ⚠ cell-cycle shift, explains ~0% of this change).

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10154.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.324×** | -33.5 | 0e+00 | 41/43 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.315×** | -22.2 | 0e+00 | 33/37 (SK-MEL-2, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.350×** | -22.0 | 0e+00 | 37/44 (CFPAC-1, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.333×** | -21.4 | 0e+00 | 33/39 (Panc 03.27, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.378×** | -20.4 | 0e+00 | 40/43 (C32, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.373×** | -19.0 | 0e+00 | 42/44 (SK-MEL-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.434×** | -17.5 | 0e+00 | 41/44 (Panc 03.27, HS-578T, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.455×** | -16.5 | 0e+00 | 37/44 (SK-MEL-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.541×** | -12.9 | 4e-36 | 35/44 (CFPAC-1, HEC-1-A, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.562×** | -12.1 | 6e-32 | 31/44 (SK-MEL-2, SW1417, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.642×** | -9.3 | 7e-19 | 32/44 (C32, A-427, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.677×** | -7.5 | 3e-12 | 26/43 (CFPAC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.755×** | -5.9 | 2e-07 | 24/44 (LoVo, LS 180, …) | top dose only | composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM | ⚠ position correction uncertain | **0.766×** | -5.6 | 1e-06 | 22/44 (A498, Panc 03.27, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.633×** | -5.0 | 2e-05 | 20/45 (SNU-423, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.788×** | -5.0 | 2e-05 | 19/44 (CFPAC-1, HepG2/C3A, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.803×** | -4.6 | 1e-04 | 23/44 (HepG2/C3A, HEC-1-A, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.829×** | -3.9 | 0.002 | 16/44 (Panc 03.27, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.830×** | -3.6 | 0.007 | 15/44 (SK-MEL-2, HOP62, …) | all doses, flat |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.887× | -3.5 | 0.009 | 13/44 (A549, A498, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.839× | -3.4 | 0.016 | 19/44 (HOP62, NCI-H1792, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10154. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 212 | 0 | 17 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0752× (z -29.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.112× (z -26.6) |
| [[CFPAC-1 (line)]] | alt | 305 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -30.8) |
| [[SK-MEL-2 (line)]] | alt | 233 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0739× (z -38.8) |
| [[HEC-1-A (line)]] | alt | 93.1 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -19.5) |
| [[NCI-H2347 (line)]] | alt | 125 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -19.0) |
| [[C32 (line)]] | wt | 133 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0911× (z -34.1) |
| [[HepG2_C3A (line)]] | wt | 212 | 0 | 10 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.155× (z -17.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.352× (z -14.7) |
| [[HS-578T (line)]] | alt | 76.3 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -22.8) |
| [[hTERT-HPNE (line)]] | wt | 152 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0907× (z -24.3) |
| [[RPMI-7951 (line)]] | alt | 138 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -23.0) |
| [[A498 (line)]] | wt | 81.4 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.181× (z -18.9) |
| [[COLO 205 (line)]] | alt | 253 | 1 (1 ⚠) | 8 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.18× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0924× (z -24.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.198× (z -23.3) |
| [[SNU-423 (line)]] | alt | 87.5 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -20.0) |
| [[SW1417 (line)]] | alt | 85.4 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.214× (z -17.0) |
| [[HOP62 (line)]] | alt | 138 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -24.8) |
| [[LoVo (line)]] | wt | 55.5 | 1 (1 ⚠) | 7 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.181× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.346× (z -18.6) |
| [[A549 (line)]] | wt | 96.1 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.217× (z -17.5) |
| [[LS 180 (line)]] | wt | 72.1 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.334× (z -11.3) |
| [[BT-474 (line)]] | alt | 65.1 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0759× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.200× (z -12.0) |
| [[A-427 (line)]] | wt | 45.9 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.241× (z -12.0) |
| [[KATO III (line)]] | alt | 62.0 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.311× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 53.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -15.5) |
| [[A-172 (line)]] | wt | 38.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -14.8) |
| [[HT-29 (line)]] | alt | 75.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -17.2) |
| [[J82 (line)]] | alt | 51.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.435× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 30.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 43.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -14.3) |
| [[NCI-H1792 (line)]] | alt | 58.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -22.2) |
| [[NCI-H460 (line)]] | wt | 29.0 | 1 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +13.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -13.2) |
| [[SW480 (line)]] | alt | 29.2 | 1 (1 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.409× (z -8.9) |
| [[HCT15 (line)]] | alt | 123 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.321× (z -14.4) |
| [[NCI-H23 (line)]] | alt | 30.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -22.0) |
| [[SW 900 (line)]] | alt | 59.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -15.5) |
| [[AsPC-1 (line)]] | alt | 29.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0898× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.359× (z -10.3) |
| [[PANC-1 (line)]] | alt | 48.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -12.8) |
| [[SW 1088 (line)]] | alt | 92.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -10.3) |
| [[SW 1271 (line)]] | alt | 68.8 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0524× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 33.2 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0530× (z -11.2) |
| [[CHP-212 (line)]] | wt | 29.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0754× (z -12.2) |
| [[Hs 766T (line)]] | wt | 30.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW48 (line)]] | wt | 40.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.152× (z -10.0) |
| [[C-33 A (line)]] | alt | 17.7 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 17.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10154), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM51-AS1]] | +0.62 | +0.57 / +0.66 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[TNFRSF11A]] | +0.61 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[UBTD1]] | +0.56 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[CXCR4]] | +0.55 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[GPR157]] | +0.54 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[ABHD17C]] | +0.52 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[TMEM158]] | +0.51 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[PDE8A]] | +0.49 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[LHX1-DT]] | +0.49 | +0.37 / +0.46 | both halves | 8e-05 |  |
| [[OTUB2]] | +0.49 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[CLEC2B]] | +0.48 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[RNF149]] | +0.47 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[TRIM62]] | +0.47 | +0.45 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IMPACT]] | -0.54 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[N6AMT1]] | -0.53 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[MAP2]] | -0.52 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[PIGO]] | -0.52 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[USP40]] | -0.52 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[HDHD2]] | -0.51 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[DCLK2]] | -0.50 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[ERCC6]] | -0.50 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[ICE2]] | -0.50 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[IL1R1]] | -0.50 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[CLCN4]] | -0.50 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[YTHDC2]] | -0.50 | -0.56 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM51-AS1]] | B | TMEM51-AS1 activity raises TMEM51's level | lines that do not express TMEM51-AS1 (13) vs lines expressing it (37) | 2.68× lower at baseline in the lines without TMEM51-AS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: RAB17, PLEKHG1, EPHA1; maybe low, not absent |
| [[HNF1B]] | B | HNF1B activity raises TMEM51's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 2.13× lower at baseline in the lines without HNF1B | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |
| [[HNF1B]] | B | HNF1B activity strengthens TMEM51's drug response | lines that do not express HNF1B (27) vs lines expressing it (18) | the lines without HNF1B respond 0.74× as strongly (z diff +1.92); strongest at Dinaciclib 0.05 µM: 0.42x vs 0.25x (z diff +3.3) | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1; target measured in part of the lines; artifact flags |
| [[CLCN4]] | B | CLCN4 activity raises TMEM51's level | lines that do not express CLCN4 (7) vs lines expressing it (43) | 1.85× lower at baseline in the lines without CLCN4 | 0.068 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[KRT7]] | B | KRT7 activity raises TMEM51's level | lines that do not express KRT7 (34) vs lines expressing it (16) | 1.54× lower at baseline in the lines without KRT7 | 0.082 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDS1]] | C | TMEM51 activity raises CDS1's level | lines that do not express TMEM51 (4) vs lines expressing it (46) | 2.60× lower at baseline in the lines without TMEM51 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ANKEF1, CEMIP2, AHR; maybe low, not absent; its own permutation p |
| [[ABHD17C]] | C | TMEM51 activity raises ABHD17C's level | lines that do not express TMEM51 (4) vs lines expressing it (46) | 3.34× lower at baseline in the lines without TMEM51 | 0.094 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ANKEF1, CEMIP2, AHR; maybe low, not absent |
| [[KHDRBS3]] | C | TMEM51 activity raises KHDRBS3's level | lines that do not express TMEM51 (4) vs lines expressing it (46) | 3.46× lower at baseline in the lines without TMEM51 | 0.095 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ANKEF1, CEMIP2, AHR; maybe low, not absent |

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.551). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.5, -2.3); signed map (-3.9, 49.7). **Vector** length 109, 31.8% of its response variance represented; |z| ≥ 3 in 1,459 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.9 | +2.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +1.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.0 | -12.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | -1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +0.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.2 | +0.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.6 | +0.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.9 | -20.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.8 | -22.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.7 | -21.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.9 | -33.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.7 | -22.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -12.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM | ⚠ position correction uncertain | -3.6 | -4.9 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -3.4 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.2 | -3.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 51 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.21 — chr1:15,152,532-15,220,478 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10199; previously C1orf72 |
| Matched by | ensembl_id |

UniProt [Q9NW97](https://www.uniprot.org/uniprotkb/Q9NW97) carries no function annotation.

**Summary**, from NCBI Gene [55092](https://www.ncbi.nlm.nih.gov/gene/55092):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25488](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25488) · Entrez [55092](https://www.ncbi.nlm.nih.gov/gene/55092) · UniProt [Q9NW97](https://www.uniprot.org/uniprotkb/Q9NW97) · Ensembl [ENSG00000171729](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171729)

## Data

Gene col 10154: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10154); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10154, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10154]; `tensor/DDL_lfc|DDL_z.npy` [10154]; `embed/gene_vectors.npy` [10154]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10154 or target_col == 10154). Every well: [[TMEM51 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM51.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
