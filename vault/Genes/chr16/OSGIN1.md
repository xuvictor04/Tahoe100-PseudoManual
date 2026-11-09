---
symbol: "OSGIN1"
type: "gene"
col: 6470
ensembl_id: "ENSG00000140961"
name: "oxidative stress induced growth inhibitor 1"
location: "16q23.3"
module: 125
arm: "+"
pooled_cpm: 9.32
n_lines_expressing: 48
n_dd_up: 33
n_dd_down: 11
n_dd_up_clean: 27
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# OSGIN1

*oxidative stress induced growth inhibitor 1* — 16q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.95× (z +17.3, q 0e+00, up in 38 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.502× (z -7.8, q 3e-12, down in 24 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.628× (z -7.5, q 2e-11, down in 24 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPLP0P2]] (+0.62, fdr 7e-06), [[KIAA1217]] (+0.61, fdr 1e-05), [[SQSTM1]] (+0.59, fdr 1e-05); moves opposite to [[NUDT21]] (-0.62, fdr 7e-06), [[ACTL6A]] (-0.61, fdr 1e-05), [[RCN2]] (-0.61, fdr 1e-05).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6470.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.95×** | +17.3 | 0e+00 | 38/42 (A-172, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.58×** | +14.5 | 7e-45 | 38/42 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.62×** | +13.8 | 1e-40 | 37/42 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.16×** | +13.0 | 1e-36 | 33/43 (PANC-1, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **3.16×** | +12.5 | 7e-34 | 38/44 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.56×** | +10.6 | 2e-24 | 37/43 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.50×** | +10.4 | 2e-23 | 32/43 (COLO 205, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.44×** | +10.1 | 4e-22 | 37/44 (HT-29, SW1417, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.32×** | +9.5 | 9e-20 | 34/43 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **2.18×** | +6.3 | 2e-08 | 22/43 (HT-29, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.74×** | +6.3 | 2e-08 | 23/43 (SW 900, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.71×** | +6.1 | 6e-08 | 22/43 (SNU-1, A498, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.75×** | +6.0 | 1e-07 | 13/29 (HCT15, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.54×** | +5.5 | 1e-06 | 18/42 (HT-29, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +5.0 | 2e-05 | 22/43 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.33×** | +5.0 | 2e-05 | 16/42 (HT-29, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **2.28×** | +4.9 | 4e-05 | 16/33 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6470.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.502×** | -7.8 | 3e-12 | 24/30 (MIA PaCa-2, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.628×** | -7.5 | 2e-11 | 24/42 (PANC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | **0.571×** | -6.3 | 4e-08 | 25/45 (NCI-H1573, Hs 766T, …) | rises with dose |  |
| [[Megestrol (drug)]] 5 µM |  | **0.675×** | -6.3 | 4e-08 | 25/45 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.617×** | -5.1 | 5e-05 | 19/25 (HT-29, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.641×** | -5.0 | 5e-05 | 21/43 (Panc 03.27, A-172, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.651×** | -4.7 | 2e-04 | 13/37 (MIA PaCa-2, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **0.710×** | -3.9 | 0.007 | 10/43 (H4, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.910× | -3.8 | 0.010 | 7/46 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.718×** | -3.8 | 0.010 | 10/43 (NCI-H1573, A549, …) | inconsistent across doses | position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.731×** | -3.4 | 0.032 | 12/43 (H4, SK-MEL-2, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.759×** | -3.1 | 0.085 | 13/43 (NCI-H1573, A549, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6470. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 13.9 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 7.35× (z +13.7) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.187× (z -11.6) |
| [[HT-29 (line)]] | alt | 24.0 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0442× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 23.9 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0759× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -10.7) |
| [[PANC-1 (line)]] | alt | 5.85 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 6.08 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.68× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -8.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 6.32 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.55× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.112× (z -9.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 12.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.72× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.0885× (z -11.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 5.12 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.04× (z +11.0) | — |
| [[NCI-H1573 (line)]] | alt | 27.7 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 5.40× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0714× (z -13.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 14.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0702× (z -12.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 6.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.06× (z +10.7) | — |
| [[CFPAC-1 (line)]] | alt | 7.68 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +9.0) | — |
| [[COLO 205 (line)]] | alt | 6.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.12× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 8.01 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -8.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 4.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.07× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 16.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0900× (z -8.6) |
| [[A-427 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.876 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6470), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPLP0P2]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[KIAA1217]] | +0.61 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[SQSTM1]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ATF4]] | +0.59 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[HMOX1]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[NECAB2]] | +0.59 | +0.65 / +0.58 | both halves | 7e-06 | ⚠ same locus (1.9 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF165]] | +0.58 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[TRAPPC3]] | +0.57 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[CRYM]] | +0.57 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[GLRX2]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[TUBB2A]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[PPIF]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[DNAJB2]] | +0.56 | +0.54 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT21]] | -0.62 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[ACTL6A]] | -0.61 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[RCN2]] | -0.61 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[METTL9]] | -0.59 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[MRE11]] | -0.58 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[SNRPG]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[SUMO1]] | -0.54 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[PIGS]] | -0.54 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[SETD3]] | -0.54 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[CPD]] | -0.54 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[ATP6AP2]] | -0.53 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[MCMBP]] | -0.52 | -0.52 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers OSGIN1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.5% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds |
| [[CREB5]] | B | CREB5 activity raises OSGIN1's level | lines that do not express CREB5 (15) vs lines expressing it (35) | 1.81× lower at baseline in the lines without CREB5 | 0.048 | ⚠ within organs, on part of the lines; also absent: LINC01828, ITPR1, ENSG00000230647 |
| [[CRYM]] | B | CRYM activity raises OSGIN1's level | lines that do not express CRYM (12) vs lines expressing it (38) | 1.62× lower at baseline in the lines without CRYM | 0.053 | ⚠ within organs, on part of the lines; also absent: GBP3, CD44, SERPINE2; maybe low, not absent |
| [[ZSCAN31]] | B | ZSCAN31 activity raises OSGIN1's level | lines that do not express ZSCAN31 (8) vs lines expressing it (42) | 1.66× lower at baseline in the lines without ZSCAN31 | 0.095 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.611). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-9.3, 43.5); signed map (36.4, 21.0). **Vector** length 104, 24.4% of its response variance represented; |z| ≥ 3 in 1,145 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.4 | +13.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +14.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +13.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.1 | +10.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.8 | +10.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.5 | +4.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.4 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +3.8 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -1.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.1 | -5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -1.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.4 | -7.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.6 | -1.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | oxidative stress induced growth inhibitor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.3 — chr16:83,931,311-83,966,332 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BDGI, OKL38 |
| Gene groups (HGNC) | Oxygenases; Oxidative stress induced growth inhibitor family |
| Hallmark sets | P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJX0](https://www.uniprot.org/uniprotkb/Q9UJX0) (Oxidative stress-induced growth inhibitor 1):

> Monooxygenase catalytic activity. Involved in regulation of cytokinesis; promotes RHOA activity, probably acting locally at the midbody in late cytokinesis. Monooxygenase activity is involved in stabilizing transient structures between daughter cells, termed intercellular bridges, before abscission. Regulates differentiation and proliferation through the regulation of cell death.

**Summary**, from NCBI Gene [29948](https://www.ncbi.nlm.nih.gov/gene/29948):

> This gene encodes an oxidative stress response protein that regulates cell death. Expression of the gene is regulated by p53 and is induced by DNA damage. The protein regulates apoptosis by inducing cytochrome c release from mitochondria. It also appears to be a key regulator of both inflammatory and anti-inflammatory molecules. The loss of this protein correlates with uncontrolled cell growth and tumor formation. Naturally occurring read-through transcription exists between this gene and the …

**Accessions** — [HGNC:30093](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30093) · Entrez [29948](https://www.ncbi.nlm.nih.gov/gene/29948) · UniProt [Q9UJX0](https://www.uniprot.org/uniprotkb/Q9UJX0) · Ensembl [ENSG00000140961](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140961)

## Data

Gene col 6470: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6470); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6470, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6470]; `tensor/DDL_lfc|DDL_z.npy` [6470]; `embed/gene_vectors.npy` [6470]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6470 or target_col == 6470). Every well: [[OSGIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSGIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
