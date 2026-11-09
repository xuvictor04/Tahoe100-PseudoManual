---
symbol: "SRCAP"
type: "gene"
col: 1286
ensembl_id: "ENSG00000080603"
name: "Snf2 related CREBBP activator protein"
location: "16p11.2"
module: 16
arm: "+"
pooled_cpm: 72.69
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 13
n_dd_up_clean: 11
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# SRCAP

*Snf2 related CREBBP activator protein* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.95× (z +11.2, q 2e-26, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.677× (z -6.6, q 3e-08, down in 43 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHTOP]] (+0.79, fdr 7e-06), [[PUF60]] (+0.78, fdr 7e-06), [[REXO1]] (+0.77, fdr 7e-06); moves opposite to [[MGST3]] (-0.70, fdr 7e-06), [[RAB6A]] (-0.70, fdr 7e-06), [[HDAC3]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1286.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +11.2 | 2e-26 | 42/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +6.9 | 1e-09 | 12/50 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.48×** | +5.7 | 2e-06 | 43/49 (COLO 205, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.61×** | +5.6 | 2e-06 | 44/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +5.5 | 4e-06 | 32/48 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.58×** | +5.4 | 5e-06 | 43/48 (LoVo, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +4.7 | 2e-04 | 36/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.11×** | +4.6 | 2e-04 | 35/48 (HEC-1-A, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +4.1 | 0.002 | 33/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.78×** | +3.6 | 0.020 | 35/49 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.028 | 29/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.043 | 33/48 (HepG2/C3A, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.085 | 24/48 (NCI-H1573, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1286.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.677×** | -6.6 | 3e-08 | 43/49 (LS 180, NCI-H23, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.608×** | -5.9 | 8e-07 | 41/48 (NCI-H1573, SW1417, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.638×** | -5.4 | 2e-05 | 34/49 (NCI-H1573, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.648×** | -5.2 | 3e-05 | 41/48 (NCI-H1573, LoVo, …) | all doses, flat | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.653×** | -5.1 | 4e-05 | 42/48 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.700×** | -4.2 | 0.002 | 32/48 (KATO III, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~20% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.702×** | -4.2 | 0.002 | 36/48 (CHP-212, HCT15, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.703×** | -4.2 | 0.002 | 34/48 (HT-29, LoVo, …) | all doses, flat | cell-cycle shift (explains ~22% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.703×** | -4.0 | 0.004 | 28/50 (LS 180, C-33 A, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.707×** | -3.8 | 0.007 | 25/45 (NCI-H2030, C32, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | **0.809×** | -3.6 | 0.017 | 26/48 (C32, RKO, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.743×** | -3.5 | 0.019 | 31/48 (SW 900, SW 1271, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.737×** | -3.4 | 0.025 | 25/48 (C32, NCI-H23, …) | top dose only | cell-cycle shift (explains ~16% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1286. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 115 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.401× (z -8.8) |
| [[LS 180 (line)]] | wt | 76.7 | 3 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -12.8) |
| [[A498 (line)]] | wt | 78.7 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -10.2) |
| [[C32 (line)]] | wt | 58.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.219× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 61.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HepG2_C3A (line)]] | wt | 96.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +8.6) | [[Omeprazole (drug)]] 0.5 µM 0.318× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 70.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 87.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -12.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 92.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.368× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[RPMI-7951 (line)]] | alt | 68.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +10.5) | [[Pimitespib (drug)]] 5 µM 0.106× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 61.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[A549 (line)]] | wt | 63.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 45.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.3) | — |
| [[CHP-212 (line)]] | wt | 67.6 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.163× (z -8.8) |
| [[COLO 205 (line)]] | alt | 79.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.75× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 58.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 41.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.8) | — |
| [[Hs 766T (line)]] | wt | 71.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 48.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 80.8 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.368× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 53.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.5) | — |
| [[LoVo (line)]] | wt | 84.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.71× (z +12.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 81.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 59.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 79.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 28.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 83.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.65× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 58.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +12.2) | — |
| [[SW 1271 (line)]] | alt | 101 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.132× (z -8.9) |
| [[SW48 (line)]] | wt | 72.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[A-172 (line)]] | wt | 64.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 81.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 101 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 99.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 82.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1286), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHTOP]] | +0.79 | +0.69 / +0.79 | both halves | 7e-06 |  |
| [[PUF60]] | +0.78 | +0.75 / +0.80 | both halves | 7e-06 |  |
| [[REXO1]] | +0.77 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[ZC3H4]] | +0.75 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[PRRC2A]] | +0.73 | +0.65 / +0.74 | both halves | 7e-06 | same gene group; STRING 477 |
| [[EPC2]] | +0.72 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[CELSR3]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[THOC6]] | +0.71 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[RBM12]] | +0.71 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[SCAF1]] | +0.71 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[IRF2BP1]] | +0.70 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[GRWD1]] | +0.70 | +0.62 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGST3]] | -0.70 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[RAB6A]] | -0.70 | -0.65 / -0.67 | both halves | 7e-06 |  |
| [[HDAC3]] | -0.69 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[ECI2]] | -0.69 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[RNF149]] | -0.68 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[SEC11A]] | -0.68 | -0.61 / -0.66 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | -0.68 | -0.68 / -0.64 | both halves | 7e-06 |  |
| [[GMCL1]] | -0.67 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[MACO1]] | -0.67 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[LMBR1L]] | -0.65 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[CARD19]] | -0.65 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[MAX]] | -0.64 | -0.59 / -0.57 | both halves | 9e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SRCAP's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HLA-F-AS1]] | B | HLA-F-AS1 activity lowers SRCAP's level | lines that do not express HLA-F-AS1 (6) vs lines expressing it (44) | 1.17× higher at baseline in the lines without HLA-F-AS1 | 0.087 | ⚠ within organs, on part of the lines; also absent: LRP1, STRIP2, SH2D4B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.640). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-17.7, -1.8); signed map (1.4, -32.9). **Vector** length 123, 39.7% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.7 | +11.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +6.9 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.3 | +2.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.6 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +4.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.0 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.4 | +2.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.0 | -5.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.7 | -5.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.6 | -0.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.5 | -5.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.2 | -3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.7 | -3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | Snf2 related CREBBP activator protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,698,209-30,741,409 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0309, SWR1, DOMO1 |
| Gene groups (HGNC) | SNF2 related family; SRCAP complex subunits; Small nucleolar RNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZRS2](https://www.uniprot.org/uniprotkb/Q6ZRS2) (Chromatin remodeling protein SRCAP):

> Acts both as a chromatin remodeler and transcription coregulator. Catalytic component of the SRCAP complex which mediates the ATP-dependent exchange of histone H2AZ/H2B dimers for nucleosomal H2A/H2B, leading to transcriptional regulation of selected genes expression through chromatin remodeling. Acts as a coactivator for CREB-mediated transcription, steroid receptor-mediated transcription, and Notch-mediated transcription.

**Summary**, from NCBI Gene [10847](https://www.ncbi.nlm.nih.gov/gene/10847):

> This gene encodes the core catalytic component of the multiprotein chromatin-remodeling SRCAP complex. The encoded protein is an ATPase that is necessary for the incorporation of the histone variant H2A.Z into nucleosomes. It can function as a transcriptional activator in Notch-mediated, CREB-mediated and steroid receptor-mediated transcription. Mutations in this gene cause Floating-Harbor syndrome, a rare disorder characterized by short stature, language deficits and dysmorphic facial …

**Accessions** — [HGNC:16974](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16974) · Entrez [10847](https://www.ncbi.nlm.nih.gov/gene/10847) · UniProt [Q6ZRS2](https://www.uniprot.org/uniprotkb/Q6ZRS2) · Ensembl [ENSG00000080603](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080603)

## Data

Gene col 1286: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1286); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1286, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1286]; `tensor/DDL_lfc|DDL_z.npy` [1286]; `embed/gene_vectors.npy` [1286]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1286 or target_col == 1286). Every well: [[SRCAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRCAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
