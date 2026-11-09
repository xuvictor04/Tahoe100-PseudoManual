---
symbol: "CLMN"
type: "gene"
col: 9216
ensembl_id: "ENSG00000165959"
name: "calmin"
location: "14q32.13"
module: 194
arm: "-"
pooled_cpm: 108.25
n_lines_expressing: 43
n_dd_up: 4
n_dd_down: 53
n_dd_up_clean: 3
n_dd_down_clean: 37
in_vector_space: true
direction_upstream: 11
direction_downstream: 14
tags: ["gene", "module/194"]
generated_by: "tahoemap"
---

# CLMN

*calmin* — 14q32.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.25× (z +5.9, q 2e-06, up in 24 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 53 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.195× (z -42.4, q 0e+00, down in 40 of 41 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RALGAPA2]] (+0.65, fdr 3e-05), [[INPP5F]] (+0.62, fdr 3e-05), [[RHPN2]] (+0.62, fdr 3e-05); moves opposite to [[PBLD]] (-0.58, fdr 6e-04), [[MAD2L1-DT]] (-0.57, fdr 5e-04), [[THBS4]] (-0.57, fdr 1e-04).
> It sits in the **-** arm of [[Module 194]].
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[GPRC5A]] → it (grade B ⚠); 14 go from it, the strongest it → [[GPRC5A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9216.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +5.9 | 2e-06 | 24/41 (RKO, HS-578T, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.28×** | +4.6 | 0.001 | 21/42 (RKO, LS 180, …) | all doses, stronger at high dose |  |
| [[Posaconazole (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.023 | 18/41 (A549, CFPAC-1, …) | top dose only | plate-row cell shift |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.039 | 17/41 (CFPAC-1, A549, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 5 µM |  | 1.18× | +3.0 | 0.26 | 7/41 (CFPAC-1, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 62 in all, 23 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 53 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9216.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.195×** | -42.4 | 0e+00 | 40/41 (C32, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.288×** | -32.2 | 0e+00 | 39/42 (CFPAC-1, C32, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.228×** | -27.0 | 0e+00 | 41/41 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.218×** | -26.8 | 0e+00 | 41/41 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.389×** | -17.3 | 0e+00 | 38/41 (C32, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.423×** | -15.1 | 0e+00 | 37/41 (SK-MEL-2, C32, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.444×** | -14.3 | 2e-44 | 39/43 (C32, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.468×** | -13.9 | 5e-42 | 37/41 (C32, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.459×** | -13.7 | 5e-41 | 34/40 (HepG2/C3A, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.482×** | -12.3 | 3e-33 | 30/38 (A-427, C32, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.515×** | -12.1 | 3e-32 | 36/41 (C32, HepG2/C3A, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.533×** | -11.5 | 6e-29 | 37/41 (NCI-H1792, HEC-1-A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.540×** | -11.3 | 8e-28 | 35/41 (C32, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.655×** | -10.9 | 4e-26 | 30/41 (C32, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.555×** | -10.4 | 1e-23 | 28/35 (C32, Panc 03.27, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.575×** | -10.1 | 2e-22 | 35/41 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.682×** | -9.9 | 2e-21 | 30/41 (SW1417, BT-474, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.370×** | -9.5 | 5e-20 | 33/42 (HEC-1-A, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.601×** | -8.8 | 5e-17 | 29/41 (C32, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9216. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 450 | 0 | 37 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0613× (z -42.5) |
| [[NCI-H1573 (line)]] | alt | 81.6 | 18 | 6 | [[Dexamethasone (drug)]] 0.5 µM 3.91× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -25.1) |
| [[NCI-H460 (line)]] | wt | 91.6 | 0 | 23 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -18.9) |
| [[HEC-1-A (line)]] | alt | 176 | 0 | 19 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -39.8) |
| [[CFPAC-1 (line)]] | alt | 363 | 0 | 18 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0900× (z -40.0) |
| [[SW1417 (line)]] | alt | 114 | 0 | 17 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -25.5) |
| [[Panc 03.27 (line)]] | alt | 343 | 0 | 16 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -31.8) |
| [[KATO III (line)]] | alt | 274 | 0 | 15 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -25.2) |
| [[SK-MEL-2 (line)]] | alt | 131 | 0 | 15 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -29.8) |
| [[SNU-423 (line)]] | alt | 124 | 0 | 15 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -20.5) |
| [[COLO 205 (line)]] | alt | 151 | 0 | 14 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0385× (z -29.2) |
| [[SW 900 (line)]] | alt | 157 | 0 | 14 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -20.9) |
| [[A549 (line)]] | wt | 161 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0977× (z -33.6) |
| [[LoVo (line)]] | wt | 93.2 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -30.3) |
| [[LS 180 (line)]] | wt | 47.7 | 1 | 10 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.13× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -21.9) |
| [[PANC-1 (line)]] | alt | 81.5 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -32.8) |
| [[BT-474 (line)]] | alt | 225 | 0 | 10 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -19.4) |
| [[Hs 766T (line)]] | wt | 117 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -21.9) |
| [[RKO (line)]] | wt | 47.1 | 1 | 9 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.21× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -21.7) |
| [[SW480 (line)]] | alt | 35.3 | 1 | 9 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.85× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -19.5) |
| [[HepG2_C3A (line)]] | wt | 165 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -25.1) |
| [[HT-29 (line)]] | alt | 181 | 0 | 9 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -20.4) |
| [[MIA PaCa-2 (line)]] | alt | 78.1 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -18.2) |
| [[NCI-H1792 (line)]] | alt | 105 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -27.3) |
| [[NCI-H2347 (line)]] | alt | 124 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -27.1) |
| [[A498 (line)]] | wt | 58.1 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -28.1) |
| [[AsPC-1 (line)]] | alt | 180 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -20.6) |
| [[HOP62 (line)]] | alt | 64.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -22.2) |
| [[A-172 (line)]] | wt | 41.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -14.7) |
| [[HCT15 (line)]] | alt | 113 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -17.9) |
| [[HS-578T (line)]] | alt | 28.6 | 1 | 4 | [[Tucidinostat (drug)]] 5 µM 2.63× (z +9.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -14.7) |
| [[SW48 (line)]] | wt | 51.7 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -10.8) |
| [[A-427 (line)]] | wt | 58.9 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.274× (z -12.7) |
| [[H4 (line)]] | wt | 46.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 92.4 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -20.8) |
| [[NCI-H23 (line)]] | alt | 34.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -14.7) |
| [[SW 1271 (line)]] | alt | 57.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 30.7 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0458× (z -16.9) |
| [[C-33 A (line)]] | alt | 29.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -12.2) |
| [[J82 (line)]] | alt | 27.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.175× (z -11.7) |
| [[AN3 CA (line)]] | alt | 26.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.1 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.2 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 96.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 19.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 46.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9216), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RALGAPA2]] | +0.65 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[INPP5F]] | +0.62 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[RHPN2]] | +0.62 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[CORO2A]] | +0.61 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[CARHSP1]] | +0.60 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[GPR160]] | +0.60 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[RAB11FIP1]] | +0.59 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[ST3GAL5]] | +0.59 | +0.54 / +0.28 | both halves | 3e-04 |  |
| [[SH3GL3]] | +0.58 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[NOS1AP]] | +0.58 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[SPATA13]] | +0.58 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[KIF13B]] | +0.57 | +0.44 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBLD]] | -0.58 | -0.60 / -0.22 | both halves | 6e-04 |  |
| [[MAD2L1-DT]] | -0.57 | -0.61 / -0.23 | both halves | 5e-04 |  |
| [[THBS4]] | -0.57 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[ANKAR]] | -0.56 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[MCPH1]] | -0.56 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[RCBTB2]] | -0.56 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[AVEN]] | -0.55 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[CLHC1]] | -0.54 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[RHBDD3]] | -0.54 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[PCNX4-DT]] | -0.54 | -0.57 / -0.26 | both halves | 4e-04 |  |
| [[KIAA0825]] | -0.54 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[TACO1]] | -0.53 | -0.55 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPRC5A]] | B | GPRC5A activity raises CLMN's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 3.34× lower at baseline in the lines without GPRC5A | 0.001 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[TNFRSF11A]] | B | TNFRSF11A activity raises CLMN's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 3.00× lower at baseline in the lines without TNFRSF11A | 0.003 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[NCMAP]] | B | NCMAP activity raises CLMN's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 2.50× lower at baseline in the lines without NCMAP | 0.008 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent |
| [[MYO1E]] | B | MYO1E activity raises CLMN's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 3.18× lower at baseline in the lines without MYO1E | 0.021 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[ENTPD2]] | B | ENTPD2 activity raises CLMN's level | lines that do not express ENTPD2 (22) vs lines expressing it (28) | 2.17× lower at baseline in the lines without ENTPD2 | 0.067 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ESRP2 |
| [[NOS1AP]] | B | NOS1AP activity raises CLMN's level | lines that do not express NOS1AP (9) vs lines expressing it (41) | 2.28× lower at baseline in the lines without NOS1AP | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, C1orf226, CMTM8; maybe low, not absent |
| [[KCNS3]] | B | KCNS3 activity raises CLMN's level | lines that do not express KCNS3 (16) vs lines expressing it (34) | 1.86× lower at baseline in the lines without KCNS3 | 0.086 | ⚠ within organs, on part of the lines; also absent: EFCAB13, JHY, SAA1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises CLMN's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.0% of all compounds | 0.089 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02211]] | B | LINC02211 activity lowers CLMN's level | lines that do not express LINC02211 (38) vs lines expressing it (12) | 2.11× higher at baseline in the lines without LINC02211 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02945, LINC01035, PSG5 |
| [[ATP11A]] | C | ATP11A activity raises CLMN's level | lines that do not express ATP11A (4) vs lines expressing it (46) | 3.64× lower at baseline in the lines without ATP11A | 0.056 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: PLEKHG3, PPP1R26, IMPA2; maybe low, not absent |
| [[RHPN2]] | C | RHPN2 activity raises CLMN's level | lines that do not express RHPN2 (4) vs lines expressing it (46) | 2.60× lower at baseline in the lines without RHPN2 | 0.085 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RASSF7, LY6E-DT; maybe low, not absent |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPRC5A]] | B | CLMN activity raises GPRC5A's level | lines that do not express CLMN (7) vs lines expressing it (43) | 5.40× lower at baseline in the lines without CLMN | 0.003 | ⚠ within organs, on part of the lines; also absent: ITPR3, NABP1, HTATIP2; maybe low, not absent |
| [[TMEM63A]] | B | CLMN activity raises TMEM63A's level | lines that do not express CLMN (7) vs lines expressing it (43) | 1.95× lower at baseline in the lines without CLMN | 0.005 | ⚠ within organs, on part of the lines; also absent: ITPR3, NABP1, HTATIP2; maybe low, not absent |
| [[CACNA2D1]] | B | CLMN activity lowers CACNA2D1's level | lines that do not express CLMN (7) vs lines expressing it (43) | 3.62× higher at baseline in the lines without CLMN | 0.008 | ⚠ within organs, on part of the lines; also absent: ITPR3, NABP1, HTATIP2; maybe low, not absent |
| [[RHPN2]] | B | CLMN activity raises RHPN2's level | lines that do not express CLMN (7) vs lines expressing it (43) | 2.95× lower at baseline in the lines without CLMN | 0.010 | ⚠ within organs, on part of the lines; also absent: ITPR3, NABP1, HTATIP2; maybe low, not absent |
| [[MYO1E]] | B | CLMN activity raises MYO1E's level | lines that do not express CLMN (7) vs lines expressing it (43) | 3.03× lower at baseline in the lines without CLMN | 0.012 | ⚠ within organs, on part of the lines; also absent: ITPR3, NABP1, HTATIP2; maybe low, not absent |
| [[ANKRD30A]] | B | CLMN activity lowers ANKRD30A's level | lines that do not express CLMN (7) vs lines expressing it (43) | 2.58× higher at baseline in the lines without CLMN | 0.015 | ⚠ within organs, on part of the lines; also absent: ITPR3, NABP1, HTATIP2; maybe low, not absent |
| [[GTF3C6]] | B | CLMN activity lowers GTF3C6's level | lines that do not express CLMN (7) vs lines expressing it (43) | 1.65× higher at baseline in the lines without CLMN | 0.015 | ⚠ within organs, on part of the lines; also absent: ITPR3, NABP1, HTATIP2; maybe low, not absent |
| [[LINC00993]] | B | CLMN activity lowers LINC00993's level | lines that do not express CLMN (7) vs lines expressing it (43) | 2.20× higher at baseline in the lines without CLMN | 0.019 | ⚠ within organs, on part of the lines; also absent: ITPR3, NABP1, HTATIP2; maybe low, not absent |
| [[BAIAP3]] | B | CLMN activity raises BAIAP3's level | lines that do not express CLMN (7) vs lines expressing it (43) | 1.95× lower at baseline in the lines without CLMN | 0.025 | ⚠ within organs, on part of the lines; also absent: ITPR3, NABP1, HTATIP2; maybe low, not absent |
| [[HPCAL1]] | B | CLMN activity raises HPCAL1's level | lines that do not express CLMN (7) vs lines expressing it (43) | 2.37× lower at baseline in the lines without CLMN | 0.036 | ⚠ within organs, on part of the lines; also absent: ITPR3, NABP1, HTATIP2; maybe low, not absent |
| [[SPATA13]] | B | CLMN activity raises SPATA13's level | lines that do not express CLMN (7) vs lines expressing it (43) | 2.28× lower at baseline in the lines without CLMN | 0.055 | ⚠ within organs, on part of the lines; also absent: ITPR3, NABP1, HTATIP2; maybe low, not absent |
| [[CORO2A]] | B | CLMN activity strengthens CORO2A's drug response | lines that do not express CLMN (7) vs lines expressing it (38) | the lines without CLMN respond 0.42× as strongly (z diff +2.23); strongest at Homoharringtonine 0.5 µM: 0.73x vs 0.34x (z diff +3.9) | 0.057 | ⚠ within organs, on part of the lines; also absent: ITPR3, NABP1, HTATIP2; maybe low, not absent; target measured in part of the lines; the reference differs; artifact flags |

## Where it sits

- **Module**: [[Module 194]]; 17 genes; this gene is in the **-** arm (projection on the module's main direction -0.641). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (6.9, 5.1); signed map (-20.0, 34.2). **Vector** length 114, 40.2% of its response variance represented; |z| ≥ 3 in 1,789 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.8 | +5.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.6 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +6.5 | +4.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.4 | -2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.2 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.1 | +1.3 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +3.0 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +2.4 |
|  | [[Bexarotene (drug)]] 5 µM |  | +1.9 | +1.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.3 | -10.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.8 | -11.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -26.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.5 | -27.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.4 | -17.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.3 | -9.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.8 | -5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -13.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -12.1 |
|  | [[EX229 (drug)]] 5 µM |  | -3.9 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | calmin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.13 — chr14:95,181,940-95,319,908 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12383, KIAA1188, KIAA0500 |
| Matched by | ensembl_id |

UniProt [Q96JQ2](https://www.uniprot.org/uniprotkb/Q96JQ2) carries no function annotation.

**Summary**, from NCBI Gene [79789](https://www.ncbi.nlm.nih.gov/gene/79789):

> Predicted to enable actin filament binding activity. Predicted to be involved in negative regulation of cell population proliferation and nuclear migration. Predicted to act upstream of or within neuron projection development. Predicted to be located in membrane. Predicted to be part of meiotic nuclear membrane microtubule tethering complex. Predicted to be active in cytoplasm and nuclear outer membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19972](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19972) · Entrez [79789](https://www.ncbi.nlm.nih.gov/gene/79789) · UniProt [Q96JQ2](https://www.uniprot.org/uniprotkb/Q96JQ2) · Ensembl [ENSG00000165959](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165959)

## Data

Gene col 9216: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9216); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9216, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9216]; `tensor/DDL_lfc|DDL_z.npy` [9216]; `embed/gene_vectors.npy` [9216]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9216 or target_col == 9216). Every well: [[CLMN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLMN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
