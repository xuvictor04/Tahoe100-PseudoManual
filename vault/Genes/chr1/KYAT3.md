---
symbol: "KYAT3"
type: "gene"
col: 6096
ensembl_id: "ENSG00000137944"
name: "kynurenine aminotransferase 3"
location: "1p22.2"
module: 219
arm: "+"
pooled_cpm: 52.97
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 25
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/219"]
generated_by: "tahoemap"
---

# KYAT3

*kynurenine aminotransferase 3* — 1p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 0.5 µM: 1.24× (z +4.2, q 0.014, up in 20 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.628× (z -12.8, q 1e-34, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GP6-AS1]] (+0.62, fdr 2e-05), [[RBMXL1]] (+0.60, fdr 4e-05, ⚠ same locus), [[DDX19B]] (+0.57, fdr 2e-05), [[DIABLO]] (+0.55, fdr 2e-05); moves opposite to [[CDK2AP1]] (-0.52, fdr 5e-05), [[SLC16A4-AS1]] (-0.52, fdr 7e-05), [[LAMTOR5-AS1]] (-0.52, fdr 3e-05).
> It is in [[Module 219]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6096.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 0.014 | 20/48 (Hs 766T, SW 900, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.076 | 14/48 (Hs 766T, J82, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.083 | 17/48 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Posaconazole (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.083 | 16/48 (NCI-H2347, BT-474, …) | top dose only | plate-row cell shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.12× | +3.1 | 0.22 | 6/48 (RKO, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6096.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.628×** | -12.8 | 1e-34 | 41/48 (HEC-1-A, A-427, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.521×** | -12.2 | 9e-32 | 40/47 (LoVo, SNU-423, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.566×** | -11.1 | 4e-26 | 38/48 (A-427, Panc 03.27, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.582×** | -10.5 | 9e-24 | 38/48 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.599×** | -10.0 | 2e-21 | 30/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.609×** | -9.6 | 5e-20 | 35/47 (NCI-H23, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.635×** | -8.8 | 8e-17 | 34/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.625×** | -8.8 | 1e-16 | 30/42 (SW480, H4, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.654×** | -8.2 | 1e-14 | 34/48 (SW480, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.636×** | -8.1 | 2e-14 | 34/44 (A-172, SW48, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.656×** | -7.9 | 2e-13 | 29/47 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.674×** | -7.7 | 8e-13 | 34/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.691×** | -6.9 | 2e-10 | 32/48 (BT-474, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.713×** | -6.3 | 1e-08 | 31/49 (A-427, BT-474, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.741×** | -5.8 | 2e-07 | 26/48 (PANC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.815×** | -5.6 | 6e-07 | 22/48 (SW 900, H4, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.626×** | -4.8 | 6e-05 | 26/49 (NCI-H23, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.646×** | -4.4 | 2e-04 | 21/48 (C32, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.802×** | -4.3 | 4e-04 | 19/48 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | 0.839× | -3.3 | 0.022 | 16/48 (C-33 A, LoVo, …) | top dose only |  |
| [[Gefitinib (drug)]] 5 µM |  | 0.847× | -3.2 | 0.025 | 12/48 (SW 900, NCI-H460, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.848× | -3.2 | 0.026 | 12/49 (RKO, AsPC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6096. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 66.4 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -13.0) ⚠ cell-cycle shift, explains ~82% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.367× (z -11.9) |
| [[PANC-1 (line)]] | alt | 90.8 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.341× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.350× (z -12.8) |
| [[SNU-423 (line)]] | alt | 67.3 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.301× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.394× (z -9.4) |
| [[LoVo (line)]] | wt | 49.7 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.373× (z -10.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.427× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 50.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.261× (z -11.0) |
| [[SW480 (line)]] | alt | 51.2 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.431× (z -10.8) |
| [[A-427 (line)]] | wt | 40.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -11.4) |
| [[Hs 766T (line)]] | wt | 75.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[HS-578T (line)]] | alt | 41.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -9.5) ⚠ cell-cycle shift, explains ~82% of this change |
| [[LS 180 (line)]] | wt | 67.1 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -10.4) |
| [[SW 900 (line)]] | alt | 39.8 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.239× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -8.9) |
| [[A549 (line)]] | wt | 34.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.262× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -10.1) |
| [[BT-474 (line)]] | alt | 46.3 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -10.4) |
| [[H4 (line)]] | wt | 50.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[KATO III (line)]] | alt | 48.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 85.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.549× (z -8.8) ⚠ cell-cycle shift, explains ~82% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.442× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 89.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.263× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[NCI-H460 (line)]] | wt | 23.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.279× (z -12.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.390× (z -8.8) |
| [[RKO (line)]] | wt | 119 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 58.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.274× (z -10.3) |
| [[A-172 (line)]] | wt | 31.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0727× (z -21.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[AsPC-1 (line)]] | alt | 43.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.288× (z -10.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 44.3 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.128× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 61.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -12.1) |
| [[HepG2_C3A (line)]] | wt | 36.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.266× (z -8.8) |
| [[J82 (line)]] | alt | 41.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -14.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 75.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 25.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 54.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SHP-77 (line)]] | alt | 53.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.313× (z -9.1) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 45.4 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0771× (z -8.7) |
| [[SW1417 (line)]] | alt | 40.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SW48 (line)]] | wt | 53.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A498 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6096), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GP6-AS1]] | +0.62 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[RBMXL1]] | +0.60 | +0.42 / +0.71 | both halves | 4e-05 | STRING 443; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[DDX19B]] | +0.57 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[DIABLO]] | +0.55 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[TANK]] | +0.54 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[DOCK6]] | +0.54 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[CAPZA1]] | +0.52 | +0.63 / +0.37 | both halves | 7e-05 |  |
| [[DCUN1D3]] | +0.52 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[MT1X]] | +0.52 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[NOSIP]] | +0.52 | +0.48 / +0.39 | both halves | 6e-05 |  |
| [[ASL]] | +0.51 | +0.56 / +0.32 | both halves | 2e-04 | pathway: Metabolism of amino acids and derivatives |
| [[ESCO1]] | +0.51 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[DDX50]] | +0.51 | +0.42 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK2AP1]] | -0.52 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[SLC16A4-AS1]] | -0.52 | -0.37 / -0.47 | both halves | 7e-05 |  |
| [[LAMTOR5-AS1]] | -0.52 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[LINC02615]] | -0.51 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[CRPPA]] | -0.50 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[IQCE]] | -0.50 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[GAS2]] | -0.50 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[ZNF362]] | -0.50 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[MYLK-AS1]] | -0.49 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[ANP32A]] | -0.49 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[VSIG10]] | -0.48 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[MTA2]] | -0.47 | -0.45 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KYAT3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 219]]; 11 genes; every member is in the + arm (projection on the module's main direction 0.470). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.44; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-32.8, 17.6); signed map (8.7, 24.7). **Vector** length 92.6, 22.9% of its response variance represented; |z| ≥ 3 in 1,136 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | -0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.1 | +3.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.9 | +0.9 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | +1.8 | +2.9 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.7 | -12.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -12.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.2 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -8.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.2 | -2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | kynurenine aminotransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.2 — chr1:88,935,773-88,992,953 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RBM1, RP11-82K18.3, KAT3, KATIII; previously CCBL2 |
| Gene groups (HGNC) | Transaminases |
| Reactome | 2 pathways, smallest: Tryptophan catabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6YP21](https://www.uniprot.org/uniprotkb/Q6YP21) (Kynurenine--oxoglutarate transaminase 3):

> Catalyzes the irreversible transamination of the L-tryptophan metabolite L-kynurenine to form kynurenic acid (KA), an intermediate in the tryptophan catabolic pathway which is also a broad spectrum antagonist of the three ionotropic excitatory amino acid receptors among others. May catalyze the beta-elimination of S-conjugates and Se-conjugates of L-(seleno)cysteine, resulting in the cleavage of the C-S or C-Se bond. Has transaminase activity towards L-kynurenine, tryptophan, phenylalanine, …

**Summary**, from NCBI Gene [56267](https://www.ncbi.nlm.nih.gov/gene/56267):

> This gene encodes an aminotransferase that transaminates kynurenine to form kynurenic acid, which is a metabolite of tryptophan. Multiple alternatively spliced transcript variants that encode different proteins have been described for this gene. This gene shares 5' exon structure with the RNA binding motif protein, X-linked-like 1 locus on chromosome 1, but the coding sequences are non-overlapping. [provided by RefSeq, Mar 2017]

**Accessions** — [HGNC:33238](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33238) · Entrez [56267](https://www.ncbi.nlm.nih.gov/gene/56267) · UniProt [Q6YP21](https://www.uniprot.org/uniprotkb/Q6YP21) · Ensembl [ENSG00000137944](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137944)

## Data

Gene col 6096: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6096); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6096, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6096]; `tensor/DDL_lfc|DDL_z.npy` [6096]; `embed/gene_vectors.npy` [6096]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6096 or target_col == 6096). Every well: [[KYAT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KYAT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
