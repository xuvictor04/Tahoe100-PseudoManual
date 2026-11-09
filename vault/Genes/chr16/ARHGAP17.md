---
symbol: "ARHGAP17"
type: "gene"
col: 6448
ensembl_id: "ENSG00000140750"
name: "Rho GTPase activating protein 17"
location: "16p12.1"
module: 214
arm: "+"
pooled_cpm: 84.64
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/214"]
generated_by: "tahoemap"
---

# ARHGAP17

*Rho GTPase activating protein 17* — 16p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.13× (z +11.3, q 5e-27, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.509× (z -10.1, q 2e-21, down in 40 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.640× (z -6.7, q 4e-09, down in 41 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1573 0.234×, AsPC-1 0.272×, A498 0.346×, LS 180 0.302×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (AsPC-1 0.392×, A549 0.449×, HT-29 0.366×, NCI-H1792 0.435×, …); [[Dinaciclib (drug)]] 5 µM in 4 lines (A549 0.225×, SW1417 0.203×, HT-29 0.167×, AsPC-1 0.251×; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.336×); [[Arbutin (drug)]] 5 µM in 1 line (SW 1088 0.0602×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP4R1]] (+0.63, fdr 1e-05), [[LRRFIP2]] (+0.63, fdr 7e-06), [[MRTFA]] (+0.62, fdr 1e-05); moves opposite to [[ADAMTSL4-AS2]] (-0.58, fdr 1e-05), [[TRIM39]] (-0.55, fdr 1e-05), [[LRIF1]] (-0.54, fdr 2e-05).
> It is in [[Module 214]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CNIH3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6448.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.13×** | +11.3 | 5e-27 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.65×** | +7.6 | 1e-11 | 37/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +7.2 | 8e-11 | 39/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.55×** | +6.6 | 6e-09 | 40/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +5.6 | 2e-06 | 35/47 (J82, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.94×** | +5.2 | 2e-05 | 38/49 (NCI-H460, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +4.9 | 7e-05 | 38/48 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +4.4 | 7e-04 | 29/48 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.098 | 20/48 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.098 | 22/48 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6448.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1573 0.234×, AsPC-1 0.272×, A498 0.346×, LS 180 0.302×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (AsPC-1 0.392×, A549 0.449×, HT-29 0.366×, NCI-H1792 0.435×, …); [[Dinaciclib (drug)]] 5 µM in 4 lines (A549 0.225×, SW1417 0.203×, HT-29 0.167×, AsPC-1 0.251×; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.336×); [[Arbutin (drug)]] 5 µM in 1 line (SW 1088 0.0602×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.509×** | -10.1 | 2e-21 | 40/49 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.550×** | -8.6 | 2e-15 | 31/42 (A549, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.640×** | -6.7 | 4e-09 | 41/48 (SNU-423, HT-29, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.740×** | -6.4 | 3e-08 | 31/49 (AsPC-1, A549, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.729×** | -4.4 | 0.001 | 26/45 (A549, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.921× | -4.2 | 0.002 | 0/50 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | **0.780×** | -3.6 | 0.028 | 28/47 (CFPAC-1, LS 180, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.789×** | -3.5 | 0.029 | 25/47 (SW 1088, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.856× | -3.3 | 0.066 | 20/48 (LoVo, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.864× | -3.1 | 0.11 | 14/48 (SNU-1, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6448. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 83.9 | 5 (1 ⚠) | 0 | [[Binimetinib (drug)]] 5 µM 2.56× (z +10.6) | — |
| [[PANC-1 (line)]] | alt | 83.1 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.34× (z +15.7) | [[Dinaciclib (drug)]] 0.5 µM 0.448× (z -8.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 62.7 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.413× (z -9.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 46.6 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.24× (z +10.9) | — |
| [[J82 (line)]] | alt | 120 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.76× (z +12.8) | — |
| [[A498 (line)]] | wt | 176 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -11.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 116 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 182 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -13.1) |
| [[HT-29 (line)]] | alt | 89.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -12.2) |
| [[hTERT-HPNE (line)]] | wt | 84.6 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.307× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[LoVo (line)]] | wt | 102 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -8.7) |
| [[SW 1088 (line)]] | alt | 110 | 0 | 3 (1 ⚠) | — | [[Arbutin (drug)]] 5 µM 0.0602× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 51.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 68.4 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 156 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 149 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -9.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 71.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -8.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 78.9 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +8.5) | [[Auranofin (drug)]] 5 µM 0.398× (z -8.8) |
| [[SW 900 (line)]] | alt | 68.1 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 86.0 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.203× (z -15.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 65.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -10.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 64.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HepG2_C3A (line)]] | wt | 125 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -10.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 79.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -9.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 85.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 56.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 34.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 63.2 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.336× (z -10.9) |
| [[SW 1271 (line)]] | alt | 55.2 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0879× (z -8.8) |
| [[A-172 (line)]] | wt | 95.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 109 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 76.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 80.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 89.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 76.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6448), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP4R1]] | +0.63 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[LRRFIP2]] | +0.63 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[MRTFA]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[KRAS]] | +0.59 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[ELMO2]] | +0.58 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[AGFG1]] | +0.55 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[TSPAN15]] | +0.54 | +0.36 / +0.56 | both halves | 9e-05 |  |
| [[TRIM37]] | +0.53 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[IFNGR1]] | +0.52 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[KPNA1]] | +0.52 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[OSBPL9]] | +0.51 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[MPPE1]] | +0.51 | +0.49 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTSL4-AS2]] | -0.58 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[TRIM39]] | -0.55 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[LRIF1]] | -0.54 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[SPRED3]] | -0.53 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[RABGEF1P3]] | -0.53 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[GPATCH2L]] | -0.52 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[MAP3K7]] | -0.52 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[PRR7-AS1]] | -0.52 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[ZNF275]] | -0.51 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[ZNF432]] | -0.51 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[FBXO41]] | -0.51 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[PRKAG1]] | -0.51 | -0.53 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNIH3]] | B | CNIH3 activity lowers ARHGAP17's level | lines that do not express CNIH3 (12) vs lines expressing it (38) | 1.32× higher at baseline in the lines without CNIH3 | 0.004 | ⚠ within organs, on part of the lines; also absent: HDGFL3, RIMKLB, ZNF793; maybe low, not absent |
| [[AKR1C2]] | B | AKR1C2 activity raises ARHGAP17's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 1.34× lower at baseline in the lines without AKR1C2 | 0.064 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2 |
| [[PLCE1]] | B | PLCE1 activity raises ARHGAP17's level | lines that do not express PLCE1 (16) vs lines expressing it (34) | 1.28× lower at baseline in the lines without PLCE1 | 0.094 | ⚠ within organs, on part of the lines; also absent: SLC46A3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 214]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.814). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.3, -11.9); signed map (-28.3, -16.1). **Vector** length 84.0, 21.9% of its response variance represented; |z| ≥ 3 in 1,044 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (drug)]] 0.5 µM |  | +4.7 | +1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.5 | +1.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.4 | +5.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.3 | +1.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.2 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +2.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.9 | -6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | +1.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -0.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.2 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +0.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.1 — chr16:24,919,389-25,015,666 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RICH1, FLJ10308, NADRIN, FLJ13219, WBP15 |
| Gene groups (HGNC) | N-BAR domain containing; AH/BAR family Rho GTPase activating proteins |
| Reactome | 9 pathways, smallest: RHOD GTPase cycle; RHOQ GTPase cycle; RAC2 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68EM7](https://www.uniprot.org/uniprotkb/Q68EM7) (Rho GTPase-activating protein 17):

> Rho GTPase-activating protein involved in the maintenance of tight junction by regulating the activity of CDC42, thereby playing a central role in apical polarity of epithelial cells. Specifically acts as a GTPase activator for the CDC42 GTPase by converting it to an inactive GDP-bound state. The complex formed with AMOT acts by regulating the uptake of polarity proteins at tight junctions, possibly by deciding whether tight junction transmembrane proteins are recycled back to the plasma …

**Summary**, from NCBI Gene [55114](https://www.ncbi.nlm.nih.gov/gene/55114):

> RICH1 is a GTPase-activating protein (GAP). GAPs stimulate the intrinsic GTP hydrolysis of small G proteins, such as RHOA (MIM 165390), RAC1 (MIM 602048), and CDC42 (MIM 116952).[supplied by OMIM, Apr 2004]

**Accessions** — [HGNC:18239](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18239) · Entrez [55114](https://www.ncbi.nlm.nih.gov/gene/55114) · UniProt [Q68EM7](https://www.uniprot.org/uniprotkb/Q68EM7) · Ensembl [ENSG00000140750](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140750)

## Data

Gene col 6448: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6448); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6448, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6448]; `tensor/DDL_lfc|DDL_z.npy` [6448]; `embed/gene_vectors.npy` [6448]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6448 or target_col == 6448). Every well: [[ARHGAP17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
