---
symbol: "GTF2H3"
type: "gene"
col: 3226
ensembl_id: "ENSG00000111358"
name: "general transcription factor IIH subunit 3"
location: "12q24.31"
module: 1
arm: "+"
pooled_cpm: 29.34
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 6
n_dd_up_clean: 17
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# GTF2H3

*general transcription factor IIH subunit 3* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.10× (z +20.4, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.630× (z -9.0, q 9e-17, down in 29 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.664× (z -8.0, q 3e-13, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GUF1]] (+0.80, fdr 7e-06), [[ICE2]] (+0.73, fdr 7e-06), [[PUS7L]] (+0.71, fdr 8e-06); moves opposite to [[UBL5]] (-0.71, fdr 7e-06), [[NENF]] (-0.69, fdr 7e-06), [[SSR4]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HLA-DRB1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3226.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.10×** | +20.4 | 0e+00 | 47/47 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.93×** | +19.4 | 0e+00 | 38/42 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.69×** | +19.3 | 0e+00 | 43/44 (SW480, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.60×** | +17.9 | 0e+00 | 36/37 (SW480, HEC-1-A, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.29×** | +16.1 | 0e+00 | 48/48 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.23×** | +15.6 | 0e+00 | 41/47 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.07×** | +14.2 | 1e-43 | 45/48 (SW480, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.11×** | +14.0 | 8e-43 | 44/48 (NCI-H1573, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.96×** | +13.1 | 1e-37 | 40/48 (SW480, A549, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.79×** | +11.4 | 2e-28 | 40/48 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.77×** | +11.1 | 4e-27 | 42/48 (C32, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.51×** | +8.0 | 8e-14 | 33/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +7.9 | 2e-13 | 31/48 (NCI-H1573, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.49×** | +7.7 | 4e-13 | 30/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.51×** | +7.7 | 4e-13 | 31/46 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.87×** | +6.4 | 7e-09 | 26/46 (PANC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.72×** | +5.5 | 1e-06 | 27/48 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.64×** | +5.0 | 1e-05 | 26/47 (Hs 766T, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.60×** | +4.8 | 4e-05 | 18/48 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +4.1 | 1e-03 | 15/48 (NCI-H1792, LOX-IMVI, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.26×** | +4.1 | 0.001 | 14/47 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.23×** | +4.0 | 0.001 | 17/47 (NCI-H460, HS-578T, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.16× | +4.0 | 0.001 | 15/48 (PANC-1, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3226.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.630×** | -9.0 | 9e-17 | 29/46 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.664×** | -8.0 | 3e-13 | 32/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.745×** | -5.8 | 2e-06 | 24/48 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.765×** | -5.2 | 2e-05 | 24/47 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.793×** | -4.5 | 7e-04 | 17/48 (Hs 766T, LS 180, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.818×** | -3.9 | 0.008 | 12/48 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[ULK-101 (drug)]] 0.05 µM |  | 0.843× | -3.2 | 0.12 | 6/48 (HS-578T, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3226. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 35.6 | 8 (5 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.17× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.24× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.439× (z -9.5) |
| [[A498 (line)]] | wt | 27.6 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.98× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 47.5 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +14.1) | [[Digitoxin (drug)]] 5 µM 0.168× (z -17.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 23.2 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.75× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.75× (z +10.1) | — |
| [[NCI-H460 (line)]] | wt | 30.7 | 4 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.32× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.441× (z -8.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 46.6 | 3 (1 ⚠) | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.07× (z +9.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.382× (z -13.0) |
| [[HOP62 (line)]] | alt | 22.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 26.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.31× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.73× (z +9.5) | — |
| [[A-172 (line)]] | wt | 20.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +11.0) | — |
| [[C-33 A (line)]] | alt | 47.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.91× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.11× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.324× (z -8.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 21.5 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.15× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 27.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.72× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[Hs 766T (line)]] | wt | 22.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.63× (z +10.2) | — |
| [[LoVo (line)]] | wt | 33.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.83× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 45.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.05× (z +10.4) | — |
| [[NCI-H1573 (line)]] | alt | 22.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +14.8) | — |
| [[SK-MEL-2 (line)]] | alt | 24.5 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.01× (z +10.6) | — |
| [[HCT15 (line)]] | alt | 43.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 19.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 20.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.56× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 26.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +13.4) | — |
| [[RKO (line)]] | wt | 40.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Digitoxin (drug)]] 5 µM 0.356× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 20.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +10.9) | — |
| [[A-427 (line)]] | wt | 42.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.85× (z +9.9) | — |
| [[A549 (line)]] | wt | 21.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.61× (z +9.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 21.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.06× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[BT-474 (line)]] | alt | 24.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +9.3) | — |
| [[C32 (line)]] | wt | 18.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +9.5) | — |
| [[KATO III (line)]] | alt | 27.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.17× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 30.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[AN3 CA (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3226), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GUF1]] | +0.80 | +0.81 / +0.80 | both halves | 7e-06 |  |
| [[ICE2]] | +0.73 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[PUS7L]] | +0.71 | +0.58 / +0.73 | both halves | 8e-06 |  |
| [[MTIF2]] | +0.70 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[FKTN]] | +0.69 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[HDHD2]] | +0.69 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[SF3A3]] | +0.69 | +0.61 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_DNA_REPAIR |
| [[MAK16]] | +0.68 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[FARSB]] | +0.68 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[GMFB]] | +0.67 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[MRRF]] | +0.67 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[BMS1]] | +0.67 | +0.64 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBL5]] | -0.71 | -0.66 / -0.68 | both halves | 7e-06 |  |
| [[NENF]] | -0.69 | -0.77 / -0.62 | both halves | 7e-06 |  |
| [[SSR4]] | -0.68 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[HIGD2A]] | -0.67 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[NDUFA2]] | -0.67 | -0.36 / -0.73 | both halves | 9e-05 |  |
| [[MAP3K3]] | -0.67 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[RABAC1]] | -0.66 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[NARF]] | -0.64 | -0.60 / -0.69 | both halves | 7e-06 |  |
| [[MZT2B]] | -0.63 | -0.70 / -0.54 | both halves | 1e-05 |  |
| [[FBXL20]] | -0.63 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[PCSK1N]] | -0.63 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[UBA52]] | -0.63 | -0.55 / -0.64 | both halves | 1e-05 | pathway: Dual Incision in GG-NER; STRING 499 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-DRB1]] | B | HLA-DRB1 activity lowers GTF2H3's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 1.32× higher at baseline in the lines without HLA-DRB1 | 0.034 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP |
| [[YPEL3]] | B | YPEL3 activity lowers GTF2H3's level | lines that do not express YPEL3 (7) vs lines expressing it (43) | 1.33× higher at baseline in the lines without YPEL3 | 0.090 | ⚠ within organs, on part of the lines; also absent: IKBKE, LTBR, RAB20 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.692). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-31.4, -16.9); signed map (0.5, -36.3). **Vector** length 109, 29.4% of its response variance represented; |z| ≥ 3 in 1,217 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.4 | +15.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.6 | +16.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +20.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.4 | +11.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.3 | +11.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.1 | +7.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.3 | +5.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.1 | +6.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.7 | +4.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -8.8 | -1.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.1 | -9.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.3 | -2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.2 | -8.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.6 | -2.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.3 | -2.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -2.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIH subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:123,633,739-123,662,604 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BTF2, TFIIH, P34 |
| Gene groups (HGNC) | Nucleotide excision repair; General transcription factor IIH complex subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 42 pathways, smallest: RNA Pol II CTD phosphorylation and interaction with CE during HIV infection; RNA Pol II CTD phosphorylation and interaction with CE; mRNA Capping |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13889](https://www.uniprot.org/uniprotkb/Q13889) (General transcription factor IIH subunit 3):

> Component of the general transcription and DNA repair factor IIH (TFIIH) core complex, which is involved in general and transcription-coupled nucleotide excision repair (NER) of damaged DNA and, when complexed to CAK, in RNA transcription by RNA polymerase II. In NER, TFIIH acts by opening DNA around the lesion to allow the excision of the damaged oligonucleotide and its replacement by a new DNA fragment. In transcription, TFIIH has an essential role in transcription initiation. When the …

**Summary**, from NCBI Gene [2967](https://www.ncbi.nlm.nih.gov/gene/2967):

> This gene encodes a member of the TFB4 family. The encoded protein is a subunit of the core-TFIIH basal transcription factor and localizes to the nucleus. The encoded protein is involved in RNA transcription by RNA polymerase II and nucleotide excision repair and associates with the Cdk-activating kinase complex. Alternative splicing results in multiple transcript variants. A related pseudogene has been identified on chromosome 14. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:4657](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4657) · Entrez [2967](https://www.ncbi.nlm.nih.gov/gene/2967) · UniProt [Q13889](https://www.uniprot.org/uniprotkb/Q13889) · Ensembl [ENSG00000111358](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111358)

## Data

Gene col 3226: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3226); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3226, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3226]; `tensor/DDL_lfc|DDL_z.npy` [3226]; `embed/gene_vectors.npy` [3226]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3226 or target_col == 3226). Every well: [[GTF2H3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF2H3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
