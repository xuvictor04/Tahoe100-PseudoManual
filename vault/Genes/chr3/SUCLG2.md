---
symbol: "SUCLG2"
type: "gene"
col: 10243
ensembl_id: "ENSG00000172340"
name: "succinate-CoA ligase GDP-forming subunit beta"
location: "3p14.1"
module: 200
arm: "+"
pooled_cpm: 136.78
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 25
n_dd_up_clean: 0
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/200"]
generated_by: "tahoemap"
---

# SUCLG2

*succinate-CoA ligase GDP-forming subunit beta* — 3p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.27× (z +4.5, q 0.003, up in 23 of 48 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 2.11×, LoVo 1.82×; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 5 µM in 1 line (NCI-H1573 1.78×; ⚠ cell-cycle shift, explains ~0% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.18×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.291× (z -29.8, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRPPRC]] (+0.65, fdr 1e-05), [[ANAPC1]] (+0.63, fdr 7e-06), [[SNX5]] (+0.63, fdr 1e-05); moves opposite to [[FAM89B]] (-0.65, fdr 1e-05), [[MEF2D]] (-0.64, fdr 3e-05), [[ZBTB7A]] (-0.62, fdr 1e-05).
> It is in [[Module 200]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RIN3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10243.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 2.11×, LoVo 1.82×; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 5 µM in 1 line (NCI-H1573 1.78×; ⚠ cell-cycle shift, explains ~0% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.18×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.27×** | +4.5 | 0.003 | 23/48 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +4.4 | 0.003 | 19/43 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +4.0 | 0.012 | 0/49 | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.11× | +3.6 | 0.052 | 2/47 (C32, SW48) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10243.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.291×** | -29.8 | 0e+00 | 46/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.440×** | -28.0 | 0e+00 | 43/47 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.339×** | -26.1 | 0e+00 | 47/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.367×** | -24.2 | 0e+00 | 46/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.497×** | -23.8 | 0e+00 | 44/48 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.553×** | -14.3 | 4e-44 | 40/47 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.545×** | -14.1 | 6e-43 | 44/47 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~20% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.588×** | -12.8 | 2e-35 | 44/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.589×** | -12.7 | 2e-35 | 34/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.371×** | -12.5 | 6e-34 | 43/48 (Panc 03.27, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.597×** | -12.4 | 1e-33 | 46/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.649×** | -10.4 | 1e-23 | 35/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.640×** | -10.3 | 2e-23 | 38/46 (J82, SNU-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.657×** | -10.1 | 2e-22 | 35/47 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.495×** | -8.8 | 3e-17 | 38/47 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -6.8 | 5e-10 | 27/47 (NCI-H23, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.604×** | -6.3 | 7e-09 | 34/48 (Panc 03.27, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10243. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 139 | 0 | 17 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -27.3) |
| [[LoVo (line)]] | wt | 125 | 1 (1 ⚠) | 15 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.82× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -28.7) |
| [[SW480 (line)]] | alt | 98.7 | 1 (1 ⚠) | 15 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.11× (z +11.3) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.185× (z -26.4) |
| [[C32 (line)]] | wt | 182 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -29.1) |
| [[HEC-1-A (line)]] | alt | 293 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -19.8) |
| [[Panc 03.27 (line)]] | alt | 196 | 0 | 12 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -22.0) |
| [[SNU-1 (line)]] | wt | 178 | 0 | 11 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0976× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -19.0) |
| [[SW1417 (line)]] | alt | 135 | 0 | 11 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -21.9) |
| [[HCT15 (line)]] | alt | 139 | 0 | 10 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.169× (z -19.5) |
| [[HOP62 (line)]] | alt | 146 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -19.2) |
| [[MIA PaCa-2 (line)]] | alt | 197 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -33.0) |
| [[PANC-1 (line)]] | alt | 117 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -20.7) |
| [[RKO (line)]] | wt | 144 | 0 | 10 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -17.9) |
| [[SNU-423 (line)]] | alt | 219 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -23.2) |
| [[J82 (line)]] | alt | 128 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.240× (z -17.1) |
| [[NCI-H1573 (line)]] | alt | 270 | 1 (1 ⚠) | 8 | [[Ixazomib citrate (drug)]] 5 µM 1.78× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -17.7) |
| [[NCI-H23 (line)]] | alt | 129 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.159× (z -20.4) |
| [[SW48 (line)]] | wt | 131 | 0 | 9 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -12.9) |
| [[A549 (line)]] | wt | 149 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -21.4) |
| [[HS-578T (line)]] | alt | 125 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -16.9) |
| [[hTERT-HPNE (line)]] | wt | 180 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -22.2) |
| [[RPMI-7951 (line)]] | alt | 185 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -19.2) |
| [[SK-MEL-2 (line)]] | alt | 194 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -24.0) |
| [[SW 900 (line)]] | alt | 114 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -15.2) |
| [[C-33 A (line)]] | alt | 150 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.187× (z -18.1) |
| [[H4 (line)]] | wt | 117 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -17.0) |
| [[KATO III (line)]] | alt | 98.6 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.248× (z -18.0) |
| [[LS 180 (line)]] | wt | 215 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -18.4) |
| [[A498 (line)]] | wt | 119 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -23.9) |
| [[HT-29 (line)]] | alt | 86.4 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.259× (z -17.4) |
| [[LOX-IMVI (line)]] | wt | 152 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.251× (z -19.8) |
| [[COLO 205 (line)]] | alt | 103 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.178× (z -18.3) |
| [[HepG2_C3A (line)]] | wt | 120 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.287× (z -13.1) |
| [[Hs 766T (line)]] | wt | 92.2 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -20.1) |
| [[A-172 (line)]] | wt | 96.7 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.410× (z -12.2) |
| [[AN3 CA (line)]] | alt | 145 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.234× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 77.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -18.5) |
| [[NCI-H2030 (line)]] | alt | 144 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -14.7) |
| [[A-427 (line)]] | wt | 86.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.334× (z -13.5) |
| [[CFPAC-1 (line)]] | alt | 71.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -18.1) |
| [[NCI-H2347 (line)]] | alt | 116 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.404× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 79.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.423× (z -9.3) |
| [[BT-474 (line)]] | alt | 92.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -10.5) |
| [[CHP-212 (line)]] | wt | 110 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -8.9) |
| [[SW 1088 (line)]] | alt | 156 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0907× (z -10.4) |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 112 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10243), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRPPRC]] | +0.65 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[ANAPC1]] | +0.63 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[SNX5]] | +0.63 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[ATIC]] | +0.62 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[TBC1D5]] | +0.62 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[NT5DC1]] | +0.62 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[UTP20]] | +0.61 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[MRPS27]] | +0.61 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[IMMP2L]] | +0.60 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[FUBP1]] | +0.58 | +0.39 / +0.59 | both halves | 6e-05 |  |
| [[ABCE1]] | +0.58 | +0.37 / +0.63 | both halves | 8e-05 |  |
| [[MCCC2]] | +0.58 | +0.41 / +0.61 | both halves | 4e-05 | STRING 400 |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM89B]] | -0.65 | -0.51 / -0.68 | both halves | 1e-05 |  |
| [[MEF2D]] | -0.64 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[ZBTB7A]] | -0.62 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[MARCHF9]] | -0.60 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[BAHD1]] | -0.59 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[PLIN3]] | -0.59 | -0.36 / -0.60 | both halves | 1e-04 |  |
| [[POLD4]] | -0.57 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[CDKN2D]] | -0.56 | -0.46 / -0.63 | both halves | 3e-05 |  |
| [[ARID3B]] | -0.56 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[RTN2]] | -0.56 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[ATG2A]] | -0.55 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[SPACDR]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RIN3]] | B | RIN3 activity raises SUCLG2's level | lines that do not express RIN3 (6) vs lines expressing it (43) | 1.78× lower at baseline in the lines without RIN3 | 0.074 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 200]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.655). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.0, -43.3); signed map (5.0, -47.2). **Vector** length 100, 33.5% of its response variance represented; |z| ≥ 3 in 1,411 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.8 | +1.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.3 | +1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.2 | -0.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.2 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | -3.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -7.6 | -12.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -23.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -14.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -4.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.8 | -12.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -4.2 | -1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -8.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.1 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | succinate-CoA ligase GDP-forming subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.1 — chr3:67,360,460-67,654,612 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Succinate-CoA ligase subunits |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 3 pathways, smallest: Citric acid cycle (TCA cycle); Mitochondrial protein degradation; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96I99](https://www.uniprot.org/uniprotkb/Q96I99) (Succinate--CoA ligase):

> GTP-specific succinyl-CoA synthetase functions in the citric acid cycle (TCA), coupling the hydrolysis of succinyl-CoA to the synthesis of GTP and thus represents the only step of substrate-level phosphorylation in the TCA. The beta subunit provides nucleotide specificity of the enzyme and binds the substrate succinate, while the binding sites for coenzyme A and phosphate are found in the alpha subunit (By similarity). Also able to act as a GTP-specific itaconyl- and malyl-CoA synthetase.

**Summary**, from NCBI Gene [8801](https://www.ncbi.nlm.nih.gov/gene/8801):

> This gene encodes a GTP-specific beta subunit of succinyl-CoA synthetase. Succinyl-CoA synthetase catalyzes the reversible reaction involving the formation of succinyl-CoA and succinate. Alternate splicing results in multiple transcript variants. Pseudogenes of this gene are found on chromosomes 5 and 12. [provided by RefSeq, Apr 2010]

**Accessions** — [HGNC:11450](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11450) · Entrez [8801](https://www.ncbi.nlm.nih.gov/gene/8801) · UniProt [Q96I99](https://www.uniprot.org/uniprotkb/Q96I99) · Ensembl [ENSG00000172340](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172340)

## Data

Gene col 10243: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10243); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10243, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10243]; `tensor/DDL_lfc|DDL_z.npy` [10243]; `embed/gene_vectors.npy` [10243]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10243 or target_col == 10243). Every well: [[SUCLG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUCLG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
