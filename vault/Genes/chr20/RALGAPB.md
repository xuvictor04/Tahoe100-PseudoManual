---
symbol: "RALGAPB"
type: "gene"
col: 9959
ensembl_id: "ENSG00000170471"
name: "Ral GTPase activating protein non-catalytic subunit beta"
location: "20q11.23"
module: 36
arm: "+"
pooled_cpm: 134.74
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# RALGAPB

*Ral GTPase activating protein non-catalytic subunit beta* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.70× (z +10.3, q 5e-22, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.460× (z -16.0, q 0e+00, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.598× (z -11.0, q 5e-26, down in 44 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 11 lines (SNU-423 0.356×, SW480 0.498×, A-172 0.419×, HT-29 0.430×, …); [[Dinaciclib (drug)]] 5 µM in 7 lines (Hs 766T 0.180×, NCI-H23 0.202×, HEC-1-A 0.226×, LoVo 0.251×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (A-172 0.263×, SK-MEL-2 0.257×, RKO 0.229×, SW48 0.163×, …; ⚠ toxic; transcription drop); [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.198×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF767P-1]] (+0.59, fdr 1e-05), [[UNC13B]] (+0.54, fdr 1e-05), [[EI24]] (+0.54, fdr 1e-05); moves opposite to [[CA8]] (-0.48, fdr 3e-05), [[DLG2]] (-0.47, fdr 2e-05), [[BTN2A3P]] (-0.46, fdr 1e-04).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9959.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.70×** | +10.3 | 5e-22 | 44/49 (SW480, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +8.8 | 4e-16 | 39/48 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.33×** | +8.8 | 4e-16 | 44/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +6.3 | 4e-08 | 32/48 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +6.3 | 4e-08 | 35/48 (SNU-1, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.031 | 24/49 (SK-MEL-2, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 1.18× | +3.5 | 0.040 | 12/48 (SNU-423, NCI-H2347, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.16× | +3.1 | 0.12 | 18/48 (CFPAC-1, NCI-H1573, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.13 | 13/48 (hTERT-HPNE, SW480, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.15× | +3.0 | 0.15 | 14/48 (CFPAC-1, Hs 766T, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9959.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 11 lines (SNU-423 0.356×, SW480 0.498×, A-172 0.419×, HT-29 0.430×, …); [[Dinaciclib (drug)]] 5 µM in 7 lines (Hs 766T 0.180×, NCI-H23 0.202×, HEC-1-A 0.226×, LoVo 0.251×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (A-172 0.263×, SK-MEL-2 0.257×, RKO 0.229×, SW48 0.163×, …; ⚠ toxic; transcription drop); [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.198×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.460×** | -16.0 | 0e+00 | 41/44 (Hs 766T, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.508×** | -13.7 | 3e-40 | 43/49 (SW1417, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.528×** | -12.6 | 2e-34 | 37/45 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.598×** | -11.0 | 5e-26 | 44/48 (SNU-423, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **0.776×** | -5.4 | 7e-06 | 29/48 (Panc 03.27, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.863× | -4.5 | 8e-04 | 21/49 (A-172, J82, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.716×** | -3.4 | 0.048 | 21/47 (RKO, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9959. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 140 | 3 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.09× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.478× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.498× (z -11.7) |
| [[A-172 (line)]] | wt | 127 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.263× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.419× (z -11.5) |
| [[LS 180 (line)]] | wt | 119 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.82× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -16.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 131 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.359× (z -13.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 153 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.400× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.430× (z -11.1) |
| [[J82 (line)]] | alt | 165 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -11.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 117 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.66× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.458× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 167 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.96× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.304× (z -14.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 128 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.30× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.499× (z -9.7) |
| [[SW1417 (line)]] | alt | 280 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -16.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 183 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -16.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 122 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.50× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -10.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 86.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.474× (z -10.0) |
| [[Hs 766T (line)]] | wt | 215 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -21.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 128 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 171 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.410× (z -11.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 164 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.457× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 175 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.481× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 139 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.513× (z -8.5) |
| [[SNU-1 (line)]] | wt | 153 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.49× (z +13.0) | — |
| [[A498 (line)]] | wt | 123 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.14× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.505× (z -8.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 156 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -16.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 110 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -13.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 152 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.12× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.358× (z -12.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 96.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.471× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 144 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -14.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 114 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.462× (z -12.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 127 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.356× (z -13.2) |
| [[SW 900 (line)]] | alt | 117 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.454× (z -9.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.380× (z -9.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 99.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -9.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 93.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.381× (z -8.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 149 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -9.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.348× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 206 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -21.3) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 122 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.198× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.414× (z -11.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -14.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 193 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 100.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 93.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 216 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9959), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF767P-1]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[UNC13B]] | +0.54 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[EI24]] | +0.54 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ZDHHC5]] | +0.53 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[TIGAR]] | +0.53 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[VPS13D]] | +0.53 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[ATG5]] | +0.52 | +0.66 / +0.40 | both halves | 5e-05 |  |
| [[BTBD10]] | +0.52 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[EHMT1]] | +0.51 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[SESN1]] | +0.50 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[EXT2]] | +0.50 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[TRAPPC10]] | +0.50 | +0.65 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CA8]] | -0.48 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[DLG2]] | -0.47 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[BTN2A3P]] | -0.46 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[SEC1P]] | -0.43 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[FAM117A]] | -0.41 | -0.37 / -0.49 | both halves | 7e-05 |  |
| [[MIR30DHG]] | -0.41 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[SLC45A3]] | -0.41 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[LGALS8]] | -0.41 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[LINC00243]] | -0.41 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[LINC00624]] | -0.41 | -0.39 / -0.46 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.457). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-19.9, 35.4); signed map (-48.4, -21.2). **Vector** length 95.0, 29.1% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +4.2 | -0.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +1.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.7 | +10.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +3.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.0 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +8.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +1.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.2 | -11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -8.0 | -0.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -0.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -0.8 |
|  | [[Infigratinib (drug)]] 5 µM |  | -1.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | Ral GTPase activating protein non-catalytic subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:38,472,816-38,578,859 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp781M2411, RalGAPbeta; previously KIAA1219 |
| Gene groups (HGNC) | Armadillo like helical domain containing; MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: Translocation of SLC2A4 (GLUT4) to the plasma membrane; Membrane Trafficking; Vesicle-mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86X10](https://www.uniprot.org/uniprotkb/Q86X10) (Ral GTPase-activating protein subunit beta):

> Non-catalytic subunit of the heterodimeric RalGAP1 and RalGAP2 complexes which act as GTPase activators for the Ras-like small GTPases RALA and RALB.

**Summary**, from NCBI Gene [57148](https://www.ncbi.nlm.nih.gov/gene/57148):

> Enables protein heterodimerization activity. Predicted to be involved in Ral protein signal transduction and activation of GTPase activity. Predicted to act upstream of or within regulation of exocyst localization and regulation of protein localization. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29221](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29221) · Entrez [57148](https://www.ncbi.nlm.nih.gov/gene/57148) · UniProt [Q86X10](https://www.uniprot.org/uniprotkb/Q86X10) · Ensembl [ENSG00000170471](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170471)

## Data

Gene col 9959: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9959); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9959, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9959]; `tensor/DDL_lfc|DDL_z.npy` [9959]; `embed/gene_vectors.npy` [9959]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9959 or target_col == 9959). Every well: [[RALGAPB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RALGAPB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
