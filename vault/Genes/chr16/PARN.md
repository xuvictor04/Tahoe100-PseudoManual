---
symbol: "PARN"
type: "gene"
col: 6444
ensembl_id: "ENSG00000140694"
name: "poly(A)-specific ribonuclease"
location: "16p13.12"
module: 36
arm: "+"
pooled_cpm: 94.84
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 22
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# PARN

*poly(A)-specific ribonuclease* — 16p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.46× (z +8.0, q 9e-13, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.461× (z -16.3, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTOR]] (+0.72, fdr 7e-06), [[IPO11]] (+0.60, fdr 7e-06), [[DDX46]] (+0.59, fdr 1e-05); moves opposite to [[DLX2]] (-0.56, fdr 1e-05), [[VAV1]] (-0.56, fdr 4e-05), [[HLA-V-1]] (-0.55, fdr 1e-04).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6444.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.46×** | +8.0 | 9e-13 | 33/48 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +6.1 | 3e-07 | 27/48 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +5.7 | 2e-06 | 26/48 (SW480, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.22×** | +4.1 | 0.007 | 23/44 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 5 µM |  | 1.17× | +3.3 | 0.10 | 12/48 (SNU-423, A549, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.16 | 15/47 (A-172, BT-474, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6444.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.461×** | -16.3 | 0e+00 | 44/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.483×** | -15.3 | 0e+00 | 41/48 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.688×** | -11.1 | 2e-26 | 37/48 (A498, J82, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.582×** | -11.0 | 7e-26 | 40/48 (J82, PANC-1, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.598×** | -10.8 | 2e-25 | 41/48 (C32, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.643×** | -9.3 | 1e-18 | 36/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.664×** | -8.6 | 5e-16 | 32/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.725×** | -6.8 | 9e-10 | 29/48 (A-427, A498, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.732×** | -6.6 | 3e-09 | 35/48 (A498, KATO III, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.740×** | -6.3 | 1e-08 | 31/48 (NCI-H460, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.743×** | -6.0 | 8e-08 | 28/47 (NCI-H2030, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **0.776×** | -5.1 | 1e-05 | 28/47 (LoVo, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.791×** | -4.9 | 3e-05 | 29/49 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.640×** | -4.9 | 3e-05 | 30/48 (LOX-IMVI, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.725×** | -4.8 | 5e-05 | 30/48 (SW480, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.858× | -4.6 | 2e-04 | 19/48 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.826×** | -4.0 | 0.002 | 20/48 (SNU-423, SW1417, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.768×** | -4.0 | 0.002 | 24/48 (KATO III, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.827×** | -3.8 | 0.004 | 20/48 (NCI-H23, AsPC-1, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.719×** | -3.6 | 0.007 | 19/48 (A498, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.811×** | -3.1 | 0.037 | 14/49 (Hs 766T, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.871× | -2.9 | 0.076 | 14/48 (NCI-H2347, C-33 A, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6444. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 72.4 | 0 | 9 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.229× (z -19.0) |
| [[A498 (line)]] | wt | 180 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -21.0) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.448× (z -10.4) |
| [[J82 (line)]] | alt | 107 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -19.4) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.325× (z -14.3) |
| [[PANC-1 (line)]] | alt | 192 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -15.3) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.404× (z -13.5) |
| [[SW1417 (line)]] | alt | 118 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -15.2) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.333× (z -13.5) |
| [[SW480 (line)]] | alt | 80.2 | 2 | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.00× (z +11.2) | [[Digitoxin (drug)]] 5 µM 0.322× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.347× (z -17.2) |
| [[A549 (line)]] | wt | 98.6 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -13.1) ⚠ cell-cycle shift, explains ~59% of this change |
| [[AsPC-1 (line)]] | alt | 101 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -18.0) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -15.9) |
| [[HT-29 (line)]] | alt | 87.8 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.372× (z -11.4) |
| [[SW 900 (line)]] | alt | 53.0 | 0 | 5 (4 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0544× (z -14.0) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.385× (z -8.8) |
| [[A-427 (line)]] | wt | 192 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.362× (z -12.9) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HepG2_C3A (line)]] | wt | 117 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.202× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.320× (z -12.1) |
| [[hTERT-HPNE (line)]] | wt | 52.0 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.222× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 85.7 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.429× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.445× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 75.8 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.68× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.408× (z -10.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.453× (z -9.0) |
| [[SNU-423 (line)]] | alt | 61.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -11.1) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.374× (z -10.5) |
| [[BT-474 (line)]] | alt | 61.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.286× (z -12.2) |
| [[C32 (line)]] | wt | 103 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.307× (z -12.6) |
| [[HOP62 (line)]] | alt | 44.7 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.321× (z -11.6) |
| [[LS 180 (line)]] | wt | 76.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.244× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.299× (z -14.0) |
| [[NCI-H2030 (line)]] | alt | 121 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.293× (z -14.7) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 80.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.330× (z -11.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 101 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.416× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.469× (z -9.2) |
| [[LoVo (line)]] | wt | 98.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.427× (z -11.7) |
| [[SHP-77 (line)]] | alt | 77.0 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.345× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 71.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.337× (z -10.9) |
| [[SNU-1 (line)]] | wt | 93.3 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.263× (z -11.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 84.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.586× (z -9.6) ⚠ cell-cycle shift, explains ~59% of this change |
| [[CFPAC-1 (line)]] | alt | 40.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.45× (z +9.0) | — |
| [[H4 (line)]] | wt | 45.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.270× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 84.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.571× (z -10.1) ⚠ cell-cycle shift, explains ~59% of this change |
| [[HS-578T (line)]] | alt | 70.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.324× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.426× (z -10.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 57.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -11.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 56.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.379× (z -8.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 114 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.317× (z -10.5) |
| [[AN3 CA (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 132 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 90.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 88.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6444), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTOR]] | +0.72 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[IPO11]] | +0.60 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[DDX46]] | +0.59 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[AAGAB]] | +0.58 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[EHMT1]] | +0.57 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[ENTPD5]] | +0.57 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[NUP93]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[PIK3R4]] | +0.57 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[TRAPPC10]] | +0.56 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[HERC2]] | +0.56 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ACTL6A]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[DROSHA]] | +0.55 | +0.46 / +0.55 | both halves | 3e-05 | STRING 695 |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLX2]] | -0.56 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[VAV1]] | -0.56 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[HLA-V-1]] | -0.55 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[LINC00958]] | -0.53 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[BTN2A2]] | -0.52 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[DDX43]] | -0.51 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[ANKRD50]] | -0.51 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[FLCN]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[XKR4]] | -0.50 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[NPHS1]] | -0.50 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[NBPF26]] | -0.50 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[MATCAP2]] | -0.50 | -0.46 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers PARN's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.604). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-8.4, -29.9); signed map (-19.4, -53.8). **Vector** length 101, 28.6% of its response variance represented; |z| ≥ 3 in 1,157 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | -0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.3 | +6.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.2 | +8.0 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | +1.9 | +1.0 |
|  | [[Dabrafenib (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.8 | +0.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -10.9 | -4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -9.6 | -4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.1 | -10.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -7.2 | -11.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -5.2 | -11.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.8 | -2.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.1 | -2.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | poly(A)-specific ribonuclease |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.12 — chr16:14,435,700-14,632,728 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DAN |
| Gene groups (HGNC) | Ribosome biogenesis factors; PARN exonuclease family |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 10 pathways, smallest: KSRP (KHSRP) binds and destabilizes mRNA; Deadenylation of mRNA; ATF4 activates genes in response to endoplasmic reticulum  stress |
| Matched by | ensembl_id |

**Function**, from UniProt [O95453](https://www.uniprot.org/uniprotkb/O95453) (Poly(A)-specific ribonuclease PARN):

> 3'-exoribonuclease that has a preference for poly(A) tails of mRNAs, thereby efficiently degrading poly(A) tails. Exonucleolytic degradation of the poly(A) tail is often the first step in the decay of eukaryotic mRNAs and is also used to silence certain maternal mRNAs translationally during oocyte maturation and early embryonic development. Interacts with both the 3'-end poly(A) tail and the 5'-end cap structure during degradation, the interaction with the cap structure being required for an …

**Summary**, from NCBI Gene [5073](https://www.ncbi.nlm.nih.gov/gene/5073):

> The protein encoded by this gene is a 3'-exoribonuclease, with similarity to the RNase D family of 3'-exonucleases. It prefers poly(A) as the substrate, hence, efficiently degrades poly(A) tails of mRNAs. Exonucleolytic degradation of the poly(A) tail is often the first step in the decay of eukaryotic mRNAs. This protein is also involved in silencing of certain maternal mRNAs during oocyte maturation and early embryonic development, as well as in nonsense-mediated decay (NMD) of mRNAs that …

**Accessions** — [HGNC:8609](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8609) · Entrez [5073](https://www.ncbi.nlm.nih.gov/gene/5073) · UniProt [O95453](https://www.uniprot.org/uniprotkb/O95453) · Ensembl [ENSG00000140694](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140694)

## Data

Gene col 6444: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6444); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6444, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6444]; `tensor/DDL_lfc|DDL_z.npy` [6444]; `embed/gene_vectors.npy` [6444]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6444 or target_col == 6444). Every well: [[PARN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
