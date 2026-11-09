---
symbol: "DNAJC7"
type: "gene"
col: 9619
ensembl_id: "ENSG00000168259"
name: "DnaJ heat shock protein family (Hsp40) member C7"
location: "17q21.2"
module: 64
arm: "+"
pooled_cpm: 101.72
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 11
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# DNAJC7

*DnaJ heat shock protein family (Hsp40) member C7* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.04× (z +19.6, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.505× (z -18.8, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMC1]] (+0.71, fdr 7e-06), [[TYW3]] (+0.69, fdr 7e-06), [[NUDT9]] (+0.68, fdr 1e-05); moves opposite to [[HYAL2]] (-0.58, fdr 3e-05), [[RELL1]] (-0.56, fdr 1e-05), [[LSM4]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9619.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.04×** | +19.6 | 0e+00 | 44/48 (HEC-1-A, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.72×** | +15.0 | 0e+00 | 46/48 (HEC-1-A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.59×** | +12.9 | 1e-35 | 43/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +12.3 | 1e-32 | 45/48 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +11.3 | 2e-27 | 43/48 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +10.7 | 1e-24 | 39/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +10.0 | 2e-21 | 28/44 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.73×** | +7.9 | 2e-13 | 39/49 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.35×** | +7.7 | 7e-13 | 28/49 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.32×** | +7.4 | 7e-12 | 31/48 (A-172, NCI-H460, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +7.1 | 7e-11 | 32/48 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.28×** | +6.8 | 6e-10 | 33/48 (HOP62, BT-474, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.59×** | +6.7 | 8e-10 | 37/45 (HEC-1-A, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.24×** | +6.0 | 1e-07 | 26/48 (HT-29, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.33×** | +5.7 | 6e-07 | 31/49 (A-427, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.47×** | +5.5 | 1e-06 | 28/48 (NCI-H1573, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +4.2 | 7e-04 | 19/48 (A498, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.058 | 10/48 (HOP62, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.23×** | +2.9 | 0.076 | 8/48 (SW480, AsPC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9619.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.505×** | -18.8 | 0e+00 | 48/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.567×** | -15.7 | 0e+00 | 47/48 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.571×** | -15.5 | 0e+00 | 47/48 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.716×** | -13.0 | 1e-36 | 41/49 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.656×** | -11.6 | 3e-29 | 44/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.699×** | -9.5 | 2e-19 | 40/48 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.784×** | -9.5 | 2e-19 | 34/48 (SW1417, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.645×** | -6.3 | 2e-08 | 34/49 (A498, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.789×** | -6.3 | 2e-08 | 26/50 (A498, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.820×** | -5.5 | 3e-06 | 28/49 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.859× | -4.2 | 0.001 | 18/48 (NCI-H2030, SK-MEL-2, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.762×** | -3.9 | 0.004 | 21/48 (H4, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.880× | -3.3 | 0.037 | 9/48 (SHP-77, Panc 03.27, …) | inconsistent across doses |  |
| [[Dorzolamide (hydrochloride) (drug)]] 5 µM |  | 0.892× | -3.0 | 0.10 | 6/48 (CHP-212, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9619. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 117 | 7 (4 ⚠) | 5 | [[Auranofin (drug)]] 5 µM 2.30× (z +16.3) | [[Panobinostat (drug)]] 5 µM 0.507× (z -13.2) |
| [[A498 (line)]] | wt | 146 | 3 (2 ⚠) | 7 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.66× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -17.5) |
| [[HOP62 (line)]] | alt | 109 | 4 (2 ⚠) | 6 | [[Auranofin (drug)]] 5 µM 2.56× (z +14.2) | [[Panobinostat (drug)]] 5 µM 0.421× (z -13.1) |
| [[PANC-1 (line)]] | alt | 61.3 | 5 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.459× (z -12.2) |
| [[SW1417 (line)]] | alt | 100.0 | 3 | 5 | [[Auranofin (drug)]] 5 µM 2.12× (z +11.6) | [[Panobinostat (drug)]] 0.5 µM 0.492× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 103 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 1.86× (z +10.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.484× (z -12.6) |
| [[J82 (line)]] | alt | 103 | 4 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.16× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.81× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.500× (z -10.0) |
| [[A-172 (line)]] | wt | 107 | 3 | 2 | [[Auranofin (drug)]] 5 µM 2.15× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.435× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 135 | 4 | 1 | [[Auranofin (drug)]] 5 µM 3.28× (z +17.7) | [[Panobinostat (drug)]] 5 µM 0.559× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 126 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -15.9) |
| [[NCI-H23 (line)]] | alt | 116 | 2 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +14.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.16× (z +10.4) | [[Belinostat (drug)]] 5 µM 0.495× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 131 | 1 | 4 | [[Auranofin (drug)]] 5 µM 2.16× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.440× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 126 | 1 | 3 | [[Bortezomib (drug)]] 0.05 µM 1.76× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.459× (z -12.5) |
| [[HT-29 (line)]] | alt | 82.5 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.31× (z +15.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 103 | 4 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.58× (z +12.3) | — |
| [[NCI-H2030 (line)]] | alt | 138 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.421× (z -12.3) |
| [[A549 (line)]] | wt | 121 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 1.92× (z +8.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.446× (z -11.4) |
| [[BT-474 (line)]] | alt | 61.0 | 2 | 1 | [[Auranofin (drug)]] 5 µM 4.77× (z +16.2) | [[Panobinostat (drug)]] 0.5 µM 0.439× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 121 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -12.6) |
| [[KATO III (line)]] | alt | 127 | 2 | 1 | [[Auranofin (drug)]] 5 µM 2.09× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.532× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 72.5 | 1 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.518× (z -8.5) |
| [[SNU-423 (line)]] | alt | 106 | 1 | 2 | [[Auranofin (drug)]] 5 µM 2.13× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.526× (z -9.1) |
| [[SW 900 (line)]] | alt | 77.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.344× (z -11.9) |
| [[A-427 (line)]] | wt | 95.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.497× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 76.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.411× (z -11.5) |
| [[CHP-212 (line)]] | wt | 196 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -12.7) |
| [[HS-578T (line)]] | alt | 94.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.27× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 80.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 102 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.526× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 125 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.04× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.533× (z -9.6) |
| [[SHP-77 (line)]] | alt | 90.7 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.34× (z +9.4) | — |
| [[C32 (line)]] | wt | 64.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.84× (z +12.7) | — |
| [[COLO 205 (line)]] | alt | 102 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.419× (z -9.2) |
| [[LoVo (line)]] | wt | 77.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.70× (z +13.9) | — |
| [[RKO (line)]] | wt | 87.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.94× (z +12.9) | — |
| [[RPMI-7951 (line)]] | alt | 92.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.29× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 102 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.86× (z +10.4) | — |
| [[SW48 (line)]] | wt | 97.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.42× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 94.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 90.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 76.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 124 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9619), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMC1]] | +0.71 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[TYW3]] | +0.69 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[NUDT9]] | +0.68 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[MRPL45]] | +0.67 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[GAS8]] | +0.67 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[UBXN4]] | +0.65 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[DNAJC2]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 | same gene group; pathway: Cellular response to heat stress; STRING 446 |
| [[MTA3]] | +0.65 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[ACIN1]] | +0.64 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[EFCAB7]] | +0.63 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[CCDC43]] | +0.63 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[ZNF426]] | +0.63 | +0.70 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HYAL2]] | -0.58 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[RELL1]] | -0.56 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[LSM4]] | -0.54 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[RASA2]] | -0.53 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[MED14]] | -0.52 | -0.49 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DNAJC7's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[JAKMIP3]] | B | JAKMIP3 activity lowers DNAJC7's level | lines that do not express JAKMIP3 (11) vs lines expressing it (39) | 1.13× higher at baseline in the lines without JAKMIP3 | 0.061 | ⚠ within organs, on part of the lines; also absent: RHOU, ABCG1, CASZ1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.840). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-19.4, 10.1); signed map (7.9, -31.4). **Vector** length 90.6, 25.5% of its response variance represented; |z| ≥ 3 in 1,293 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Hedgehog 'on' state* (reactome, mean cos +0.51 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.2 | +19.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.6 | +11.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.3 | +15.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.5 | +12.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.0 | +6.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.9 | +5.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.9 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +4.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | -4.3 | +4.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -3.9 | -6.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -9.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -13.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.7 | -11.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -9.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -3.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.8 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | +0.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.7 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:41,976,421-42,021,376 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TPR2; previously TTC2 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins; Tetratricopeptide repeat domain containing |
| Reactome | 4 pathways, smallest: Regulation of HSF1-mediated heat shock response; Cellular response to heat stress; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99615](https://www.uniprot.org/uniprotkb/Q99615) (DnaJ homolog subfamily C member 7):

> Acts as a co-chaperone regulating the molecular chaperones HSP70 and HSP90 in folding of steroid receptors, such as the glucocorticoid receptor and the progesterone receptor. Proposed to act as a recycling chaperone by facilitating the return of chaperone substrates to early stages of chaperoning if further folding is required. In vitro, induces ATP-independent dissociation of HSP90 but not of HSP70 from the chaperone-substrate complexes. Recruits NR1I3 to the cytoplasm (By similarity).

**Summary**, from NCBI Gene [7266](https://www.ncbi.nlm.nih.gov/gene/7266):

> This gene encodes a member of the DNAJ heat shock protein 40 family of proteins that is characterized by two N-terminal tetratricopeptide repeat domains and a C-terminal DNAJ domain. This protein binds the chaperone proteins heat shock proteins 70 and 90 in an ATP-dependent manner and may function as a co-chaperone. Pseudogenes of this gene are found on chromosomes 1 and 6. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:12392](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12392) · Entrez [7266](https://www.ncbi.nlm.nih.gov/gene/7266) · UniProt [Q99615](https://www.uniprot.org/uniprotkb/Q99615) · Ensembl [ENSG00000168259](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168259)

## Data

Gene col 9619: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9619); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9619, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9619]; `tensor/DDL_lfc|DDL_z.npy` [9619]; `embed/gene_vectors.npy` [9619]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9619 or target_col == 9619). Every well: [[DNAJC7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
