---
symbol: "ITGA1"
type: "gene"
col: 13152
ensembl_id: "ENSG00000213949"
name: "integrin subunit alpha 1"
location: "5q11.2"
module: 228
arm: "+"
pooled_cpm: 75.02
n_lines_expressing: 32
n_dd_up: 14
n_dd_down: 20
n_dd_up_clean: 12
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 10
direction_downstream: 28
tags: ["gene", "module/228"]
generated_by: "tahoemap"
---

# ITGA1

*integrin subunit alpha 1* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.64× (z +15.3, q 0e+00, up in 21 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.558× (z -12.7, q 5e-34, down in 25 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHST15]] (+0.57, fdr 2e-05), [[PROX1-AS1]] (+0.54, fdr 3e-05), [[SLCO5A1]] (+0.53, fdr 3e-05); moves opposite to [[NCOA6]] (-0.51, fdr 1e-05), [[ABCC10]] (-0.49, fdr 8e-05), [[STIMATE]] (-0.49, fdr 5e-05).
> It is in [[Module 228]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[IL19]] → it (grade B ⚠); 28 go from it, the strongest it → [[PELO]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13152.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +15.3 | 0e+00 | 21/30 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +15.0 | 0e+00 | 13/27 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +12.3 | 3e-32 | 23/31 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +11.3 | 1e-27 | 11/31 (A498, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +9.7 | 3e-20 | 16/30 (J82, H4, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +9.7 | 3e-20 | 19/32 (SK-MEL-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.62×** | +5.5 | 3e-06 | 14/31 (J82, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.2 | 1e-05 | 13/30 (HS-578T, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[4EGI-1 (drug)]] 5 µM |  | **1.51×** | +4.7 | 1e-04 | 10/30 (NCI-H1792, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +4.7 | 1e-04 | 12/30 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.43×** | +4.1 | 0.002 | 10/25 (A549, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.003 | 14/30 (Panc 03.27, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.7 | 0.010 | 17/30 (J82, HS-578T, …) | top dose only | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +3.6 | 0.011 | 6/30 (A-172, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.6 | 0.013 | 8/31 (LS 180, NCI-H2030, …) | all doses, flat | composition shift |
| [[Sapanisertib (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.015 | 11/31 (HT-29, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Afatinib (drug)]] 0.5 µM |  | 1.13× | +3.4 | 0.017 | 3/31 (HT-29, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.17× | +3.4 | 0.017 | 8/30 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.050 | 2/30 (COLO 205, J82) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13152.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.558×** | -12.7 | 5e-34 | 25/30 (HepG2/C3A, SW 900, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.611×** | -10.7 | 3e-24 | 23/30 (HepG2/C3A, SW 900, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.727×** | -6.9 | 8e-10 | 19/30 (COLO 205, SW 900, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.552×** | -6.8 | 2e-09 | 17/30 (COLO 205, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.740×** | -6.5 | 7e-09 | 16/30 (HepG2/C3A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.811×** | -6.4 | 1e-08 | 16/31 (HepG2/C3A, SW 900, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.760×** | -5.7 | 8e-07 | 19/29 (A-172, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.790×** | -5.1 | 2e-05 | 15/30 (COLO 205, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.793×** | -4.8 | 8e-05 | 13/29 (HepG2/C3A, SNU-423, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.855× | -4.8 | 9e-05 | 13/30 (hTERT-HPNE, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.802×** | -4.8 | 9e-05 | 14/30 (HepG2/C3A, SW480, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.662×** | -4.7 | 1e-04 | 16/31 (NCI-H1792, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.809×** | -4.6 | 2e-04 | 14/30 (HepG2/C3A, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.815×** | -4.4 | 4e-04 | 18/30 (HepG2/C3A, SW 900, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.818×** | -4.4 | 5e-04 | 13/30 (SW 900, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.691×** | -4.2 | 9e-04 | 16/30 (SW 900, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.695×** | -4.1 | 0.001 | 14/28 (COLO 205, hTERT-HPNE, …) | rises with dose | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.876× | -4.1 | 0.001 | 12/30 (SW 900, CHP-212, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.832×** | -4.0 | 0.002 | 16/30 (SW480, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13152. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 1,141 | 0 | 27 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -16.6) |
| [[HepG2_C3A (line)]] | wt | 344 | 0 | 15 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0782× (z -20.3) |
| [[COLO 205 (line)]] | alt | 187 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -19.8) |
| [[A-172 (line)]] | wt | 47.3 | 3 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.90× (z +10.8) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.39× (z +9.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.155× (z -14.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.271× (z -10.3) |
| [[HS-578T (line)]] | alt | 45.3 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +16.0) | — |
| [[H4 (line)]] | wt | 125 | 2 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +19.0) | [[Panobinostat (drug)]] 5 µM 0.226× (z -12.4) |
| [[J82 (line)]] | alt | 164 | 3 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +25.9) | [[Panobinostat (drug)]] 5 µM 0.355× (z -12.0) |
| [[SW480 (line)]] | alt | 51.3 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.265× (z -12.7) |
| [[hTERT-HPNE (line)]] | wt | 246 | 2 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.232× (z -12.9) |
| [[A498 (line)]] | wt | 85.5 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.86× (z +13.8) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +12.2) | — |
| [[LoVo (line)]] | wt | 32.6 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.52× (z +11.4) | — |
| [[NCI-H460 (line)]] | wt | 41.0 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.30× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 22.9 | 3 (1 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 6.30× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 63.5 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.311× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 176 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -9.0) |
| [[CHP-212 (line)]] | wt | 319 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.193× (z -9.9) |
| [[HT-29 (line)]] | alt | 148 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.270× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 33.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +12.7) | — |
| [[NCI-H2347 (line)]] | alt | 125 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +12.6) | — |
| [[A549 (line)]] | wt | 23.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.23× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 22.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +12.3) | — |
| [[LOX-IMVI (line)]] | wt | 25.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +11.4) | — |
| [[LS 180 (line)]] | wt | 19.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.08× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 82.3 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.642× (z -12.3) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 75.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 194 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.303× (z -9.0) |
| [[SW 1088 (line)]] | alt | 80.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.84× (z +9.8) | — |
| [[A-427 (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.93 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.16 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 57.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 9.82 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 13.3 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.50 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.93 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.72 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.42 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.66 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.50 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13152), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHST15]] | +0.57 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[PROX1-AS1]] | +0.54 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[SLCO5A1]] | +0.53 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[EPHB2]] | +0.52 | +0.48 / +0.49 | both halves | 2e-05 | pathway: L1CAM interactions |
| [[ABCA10]] | +0.52 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[TMEM163]] | +0.51 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[IL19]] | +0.51 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[DNAH17]] | +0.51 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[BMP2]] | +0.51 | +0.43 / +0.50 | both halves | 3e-05 | pathway: Extracellular matrix organization |
| [[RGL1]] | +0.50 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[DKK2]] | +0.50 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[NOTCH2NLA]] | +0.50 | +0.46 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCOA6]] | -0.51 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[ABCC10]] | -0.49 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[STIMATE]] | -0.49 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[HERC2P9]] | -0.47 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[CDIN1]] | -0.47 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[HERC2P2]] | -0.47 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[AP2A2]] | -0.44 | -0.46 / -0.31 | both halves | 2e-04 | pathway: L1CAM interactions |
| [[CHST10]] | -0.44 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[CROT]] | -0.44 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[ZNF449]] | -0.44 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[DROSHA]] | -0.43 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[TMEM139-AS1]] | -0.43 | -0.48 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL19]] | B | IL19 activity raises ITGA1's level | lines that do not express IL19 (23) vs lines expressing it (27) | 2.28× lower at baseline in the lines without IL19 | 0.037 | ⚠ within organs, on part of the lines; also absent: PKHD1, IHO1, CASC20; maybe low, not absent |
| [[MAML2]] | B | MAML2 activity raises ITGA1's level | lines that do not express MAML2 (8) vs lines expressing it (42) | 4.58× lower at baseline in the lines without MAML2 | 0.039 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| [[BMP2]] | B | BMP2 activity raises ITGA1's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 2.58× lower at baseline in the lines without BMP2 | 0.057 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[KCNIP4]] | B | KCNIP4 activity raises ITGA1's level | lines that do not express KCNIP4 (6) vs lines expressing it (44) | 4.04× lower at baseline in the lines without KCNIP4 | 0.076 | ⚠ within organs, on part of the lines; also absent: MLLT3, TEX9, MAMDC2-AS1; maybe low, not absent |
| [[MILR1]] | C | MILR1 activity raises ITGA1's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 4.13× lower at baseline in the lines without MILR1 | 0.001 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1; co-absent with the target |
| [[MIR3142HG]] | C | MIR3142HG activity raises ITGA1's level | lines that do not express MIR3142HG (26) vs lines expressing it (24) | 3.51× lower at baseline in the lines without MIR3142HG | 0.005 | ⚠ within organs, on part of the lines; also absent: CTHRC1, IL6, ENSG00000291130; co-absent with the target |
| [[COL7A1]] | C | COL7A1 activity raises ITGA1's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 3.87× lower at baseline in the lines without COL7A1 | 0.008 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent; co-absent with the target |
| [[LINC00973]] | C | LINC00973 activity raises ITGA1's level | lines that do not express LINC00973 (23) vs lines expressing it (27) | 3.55× lower at baseline in the lines without LINC00973 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000239462, IL11, BICC1; co-absent with the target |
| [[MAN1A1]] | C | MAN1A1 activity raises ITGA1's level | lines that do not express MAN1A1 (20) vs lines expressing it (30) | 3.69× lower at baseline in the lines without MAN1A1 | 0.032 | ⚠ within organs, on part of the lines; also absent: BDKRB2, TMEM200A, EVA1A; co-absent with the target |
| [[PTGS2]] | C | PTGS2 activity raises ITGA1's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 3.28× lower at baseline in the lines without PTGS2 | 0.067 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4; co-absent with the target |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 21, C 7. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PELO]] | B | ITGA1 activity raises PELO's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 2.53× lower at baseline in the lines without ITGA1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |
| [[MAML2]] | B | ITGA1 activity raises MAML2's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 2.73× lower at baseline in the lines without ITGA1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |
| [[PTPRE]] | B | ITGA1 activity raises PTPRE's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 2.35× lower at baseline in the lines without ITGA1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |
| [[KCNIP4]] | B | ITGA1 activity raises KCNIP4's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 1.92× lower at baseline in the lines without ITGA1 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |
| [[VDR]] | B | ITGA1 activity raises VDR's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 2.03× lower at baseline in the lines without ITGA1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |
| [[EPHB6]] | B | ITGA1 activity raises EPHB6's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 1.99× lower at baseline in the lines without ITGA1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |
| [[CD82]] | B | ITGA1 activity raises CD82's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 2.54× lower at baseline in the lines without ITGA1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |
| [[IRAK2]] | B | ITGA1 activity raises IRAK2's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 2.26× lower at baseline in the lines without ITGA1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |
| [[NOTCH2NLB]] | B | ITGA1 activity raises NOTCH2NLB's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 1.55× lower at baseline in the lines without ITGA1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |
| [[EP400]] | B | ITGA1 activity lowers EP400's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 1.15× higher at baseline in the lines without ITGA1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |
| [[RASSF5]] | B | ITGA1 activity raises RASSF5's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 1.86× lower at baseline in the lines without ITGA1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |
| [[IER3]] | B | ITGA1 activity raises IER3's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 2.03× lower at baseline in the lines without ITGA1 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |

## Where it sits

- **Module**: [[Module 228]]; 8 genes; every member is in the + arm (projection on the module's main direction 0.664). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.9, -1.2); signed map (43.7, 14.3). **Vector** length 107, 26.7% of its response variance represented; |z| ≥ 3 in 1,125 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.7 | +15.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +11.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.6 | +12.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.0 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +3.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | -2.2 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -3.8 | -4.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.7 | -4.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.5 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.9 | -6.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.9 | -6.4 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.2 — chr5:52,787,916-52,959,209 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VLA1, CD49a |
| Gene groups (HGNC) | CD molecules; Integrin alpha subunits |
| Reactome | 13 pathways, smallest: CHL1 interactions; Platelet Adhesion to exposed collagen; Other semaphorin interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [P56199](https://www.uniprot.org/uniprotkb/P56199) (Integrin alpha-1):

> Integrin alpha-1/beta-1 is a receptor for laminin and collagen. It recognizes the proline-hydroxylated sequence G-F-P-G-E-R in collagen. Involved in anchorage-dependent, negative regulation of EGF-stimulated cell growth.

**Summary**, from NCBI Gene [3672](https://www.ncbi.nlm.nih.gov/gene/3672):

> This gene encodes the alpha 1 subunit of integrin receptors. This protein heterodimerizes with the beta 1 subunit to form a cell-surface receptor for collagen and laminin. The heterodimeric receptor is involved in cell-cell adhesion and may play a role in inflammation and fibrosis. The alpha 1 subunit contains an inserted (I) von Willebrand factor type I domain which is thought to be involved in collagen binding. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6134](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6134) · Entrez [3672](https://www.ncbi.nlm.nih.gov/gene/3672) · UniProt [P56199](https://www.uniprot.org/uniprotkb/P56199) · Ensembl [ENSG00000213949](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213949)

## Data

Gene col 13152: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13152); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13152, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13152]; `tensor/DDL_lfc|DDL_z.npy` [13152]; `embed/gene_vectors.npy` [13152]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13152 or target_col == 13152). Every well: [[ITGA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
