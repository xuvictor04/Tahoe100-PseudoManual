---
symbol: "GPD2"
type: "gene"
col: 3628
ensembl_id: "ENSG00000115159"
name: "glycerol-3-phosphate dehydrogenase 2"
location: "2q24.1"
module: 25
arm: "+"
pooled_cpm: 103.4
n_lines_expressing: 48
n_dd_up: 3
n_dd_down: 37
n_dd_up_clean: 1
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# GPD2

*glycerol-3-phosphate dehydrogenase 2* — 2q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.38× (z +7.5, q 3e-11, up in 30 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 1.29× (z +5.7, q 2e-06, up in 25 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 2.56×, PANC-1 1.93×; ⚠ toxic; transcription drop); [[Selinexor (drug)]] 5 µM in 1 line (J82 1.74×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (J82 2.21×; ⚠ cell-cycle shift, explains ~28% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (J82 2.02×); [[Homoharringtonine (drug)]] 5 µM in 1 line (J82 1.64×); [[Cobimetinib (drug)]] 5 µM in 1 line (A549 2.39×).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.408× (z -29.4, q 0e+00, down in 44 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM237]] (+0.66, fdr 8e-06), [[HACD2]] (+0.66, fdr 1e-05), [[TMEM123]] (+0.64, fdr 7e-06); moves opposite to [[DNAAF9]] (-0.56, fdr 3e-05), [[ANKS3]] (-0.55, fdr 6e-05), [[RBAK-RBAKDN]] (-0.54, fdr 2e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3628.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 2.56×, PANC-1 1.93×; ⚠ toxic; transcription drop); [[Selinexor (drug)]] 5 µM in 1 line (J82 1.74×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (J82 2.21×; ⚠ cell-cycle shift, explains ~28% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (J82 2.02×); [[Homoharringtonine (drug)]] 5 µM in 1 line (J82 1.64×); [[Cobimetinib (drug)]] 5 µM in 1 line (A549 2.39×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +7.5 | 3e-11 | 30/47 (HOP62, C32, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +6.5 | 2e-08 | 27/42 (SK-MEL-2, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +5.7 | 2e-06 | 25/45 (A549, A498, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.17× | +3.5 | 0.049 | 19/46 (A549, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.15× | +3.5 | 0.049 | 16/48 (NCI-H2347, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.16× | +3.3 | 0.095 | 13/46 (MIA PaCa-2, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.10× | +3.2 | 0.095 | 10/46 (NCI-H2347, A549, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 16 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3628.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.408×** | -29.4 | 0e+00 | 44/46 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.319×** | -26.5 | 0e+00 | 46/46 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.340×** | -25.0 | 0e+00 | 46/46 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.392×** | -21.8 | 0e+00 | 46/46 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.569×** | -12.4 | 5e-33 | 40/46 (HT-29, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.614×** | -11.3 | 1e-27 | 38/46 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.632×** | -10.2 | 1e-22 | 34/46 (COLO 205, AsPC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.649×** | -10.0 | 9e-22 | 35/46 (LS 180, SW48, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.675×** | -9.1 | 6e-18 | 31/46 (BT-474, SW1417, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.679×** | -9.0 | 2e-17 | 37/46 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.689×** | -8.6 | 4e-16 | 37/46 (AsPC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.693×** | -8.5 | 1e-15 | 30/46 (LS 180, AsPC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.509×** | -8.2 | 1e-14 | 33/43 (MIA PaCa-2, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.718×** | -7.7 | 7e-13 | 32/46 (LS 180, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.732×** | -7.2 | 2e-11 | 33/46 (PANC-1, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.811×** | -6.8 | 3e-10 | 25/47 (SW 900, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.629×** | -5.6 | 6e-07 | 24/47 (LS 180, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.843× | -5.5 | 8e-07 | 21/46 (LOX-IMVI, NCI-H2030, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.674×** | -4.8 | 4e-05 | 23/46 (SW1417, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3628. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 203 | 0 | 14 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0887× (z -33.2) |
| [[SW1417 (line)]] | alt | 138 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.287× (z -17.8) |
| [[BT-474 (line)]] | alt | 155 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.281× (z -15.5) |
| [[NCI-H1573 (line)]] | alt | 85.7 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -24.0) |
| [[PANC-1 (line)]] | alt | 56.3 | 1 (1 ⚠) | 8 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.93× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -18.8) |
| [[AsPC-1 (line)]] | alt | 218 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.264× (z -16.2) |
| [[LoVo (line)]] | wt | 136 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.169× (z -25.7) |
| [[COLO 205 (line)]] | alt | 78.4 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -19.9) |
| [[HT-29 (line)]] | alt | 105 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.204× (z -18.4) |
| [[J82 (line)]] | alt | 93.9 | 4 (2 ⚠) | 3 | [[Selinexor (drug)]] 5 µM 1.74× (z +9.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.02× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -17.1) |
| [[SW 900 (line)]] | alt | 155 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -14.4) |
| [[HEC-1-A (line)]] | alt | 116 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -24.5) |
| [[LOX-IMVI (line)]] | wt | 82.3 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -20.1) |
| [[NCI-H460 (line)]] | wt | 165 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.281× (z -17.2) |
| [[C32 (line)]] | wt | 104 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -15.7) |
| [[Hs 766T (line)]] | wt | 92.0 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.208× (z -15.5) |
| [[KATO III (line)]] | alt | 95.0 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.143× (z -22.7) |
| [[NCI-H1792 (line)]] | alt | 130 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -20.0) |
| [[NCI-H2347 (line)]] | alt | 155 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -18.2) |
| [[Panc 03.27 (line)]] | alt | 101 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -14.4) |
| [[SNU-1 (line)]] | wt | 137 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -14.5) |
| [[SNU-423 (line)]] | alt | 53.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -18.9) |
| [[SW48 (line)]] | wt | 120 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.188× (z -14.9) |
| [[SW480 (line)]] | alt | 89.4 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.212× (z -23.1) |
| [[A549 (line)]] | wt | 114 | 1 | 3 | [[Cobimetinib (drug)]] 5 µM 2.39× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -17.7) |
| [[HCT15 (line)]] | alt | 86.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -12.0) |
| [[HS-578T (line)]] | alt | 51.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -15.1) |
| [[NCI-H2030 (line)]] | alt | 177 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -19.2) |
| [[NCI-H23 (line)]] | alt | 115 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -24.1) |
| [[SHP-77 (line)]] | alt | 98.3 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -17.4) |
| [[CFPAC-1 (line)]] | alt | 54.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -15.6) |
| [[MIA PaCa-2 (line)]] | alt | 72.8 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.265× (z -13.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.435× (z -12.3) |
| [[RPMI-7951 (line)]] | alt | 123 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.301× (z -11.4) |
| [[A-427 (line)]] | wt | 100 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.337× (z -13.7) |
| [[AN3 CA (line)]] | alt | 124 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -12.6) |
| [[H4 (line)]] | wt | 67.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -12.1) |
| [[RKO (line)]] | wt | 73.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.339× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 76.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.56× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -15.7) |
| [[A-172 (line)]] | wt | 57.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -9.6) |
| [[A498 (line)]] | wt | 87.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.85 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.80 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 90.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3628), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM237]] | +0.66 | +0.57 / +0.62 | both halves | 8e-06 |  |
| [[HACD2]] | +0.66 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[TMEM123]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[GALNT7]] | +0.63 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[ERAP1]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[C5orf15]] | +0.58 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[HELLS]] | +0.57 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[PRTFDC1]] | +0.57 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[MOB1A]] | +0.57 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[TMX1]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[DHFR]] | +0.55 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[OXCT1]] | +0.55 | +0.28 / +0.53 | both halves | 3e-04 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF9]] | -0.56 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[ANKS3]] | -0.55 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[RBAK-RBAKDN]] | -0.54 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[METRNL]] | -0.54 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[ATG4B]] | -0.53 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[TFAP2E]] | -0.52 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[MPP3]] | -0.52 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[RGP1]] | -0.52 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[GPSM1]] | -0.52 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[MPHOSPH10]] | -0.51 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[RUSC2]] | -0.51 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[CDC34]] | -0.51 | -0.34 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.520). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-28.8, -17.7); signed map (-18.0, -39.4). **Vector** length 110, 34.2% of its response variance represented; |z| ≥ 3 in 1,544 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.4 | +1.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.3 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +0.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +2.7 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -6.0 | -12.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.7 | -6.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.8 | -4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.6 | -4.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.6 | -8.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | -3.3 | -4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.3 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | glycerol-3-phosphate dehydrogenase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.1 — chr2:156,435,290-156,613,735 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | EF-hand domain containing; Flavoproteins; Glycerol-3-phosphate dehydrogenases |
| Hallmark sets | FATTY_ACID_METABOLISM, COMPLEMENT, ADIPOGENESIS |
| Reactome | 6 pathways, smallest: Triglyceride catabolism; Triglyceride metabolism; Synthesis of PA |
| Matched by | ensembl_id |

**Function**, from UniProt [P43304](https://www.uniprot.org/uniprotkb/P43304) (Glycerol-3-phosphate dehydrogenase, mitochondrial):

> Calcium-responsive mitochondrial glycerol-3-phosphate dehydrogenase which seems to be a key component of the pancreatic beta-cell glucose-sensing device.

**Summary**, from NCBI Gene [2820](https://www.ncbi.nlm.nih.gov/gene/2820):

> The protein encoded by this gene localizes to the inner mitochondrial membrane and catalyzes the conversion of glycerol-3-phosphate to dihydroxyacetone phosphate, using FAD as a cofactor. Along with GDP1, the encoded protein constitutes the glycerol phosphate shuttle, which reoxidizes NADH formed during glycolysis. Two transcript variants encoding the same protein have been found for this gene.[provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:4456](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4456) · Entrez [2820](https://www.ncbi.nlm.nih.gov/gene/2820) · UniProt [P43304](https://www.uniprot.org/uniprotkb/P43304) · Ensembl [ENSG00000115159](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115159)

## Data

Gene col 3628: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3628); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3628, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3628]; `tensor/DDL_lfc|DDL_z.npy` [3628]; `embed/gene_vectors.npy` [3628]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3628 or target_col == 3628). Every well: [[GPD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
