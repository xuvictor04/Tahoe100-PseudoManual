---
symbol: "FCHO2"
type: "gene"
col: 8042
ensembl_id: "ENSG00000157107"
name: "FCH and mu domain containing endocytic adaptor 2"
location: "5q13.2"
module: 234
arm: "+"
pooled_cpm: 141.01
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 22
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/234"]
generated_by: "tahoemap"
---

# FCHO2

*FCH and mu domain containing endocytic adaptor 2* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.36× (z +5.6, q 1e-05, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.589× (z -13.8, q 3e-40, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP22]] (+0.63, fdr 7e-06), [[BRD3]] (+0.59, fdr 9e-05), [[BRWD1]] (+0.57, fdr 1e-05); moves opposite to [[ZNF628]] (-0.56, fdr 1e-05), [[TRIM16]] (-0.55, fdr 1e-05), [[XKR6]] (-0.50, fdr 3e-05).
> It is in [[Module 234]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8042.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.36×** | +5.6 | 1e-05 | 30/48 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[BAY1125976 (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.052 | 28/48 (AsPC-1, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.085 | 23/48 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8042.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.589×** | -13.8 | 3e-40 | 37/48 (NCI-H1573, SNU-423, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.514×** | -12.2 | 9e-32 | 46/48 (LOX-IMVI, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.564×** | -10.5 | 1e-23 | 36/49 (C32, HOP62, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.564×** | -10.5 | 1e-23 | 46/48 (A549, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.605×** | -8.9 | 9e-17 | 35/44 (SK-MEL-2, NCI-H23, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.628×** | -8.5 | 1e-15 | 39/48 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.637×** | -8.3 | 1e-14 | 43/48 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.617×** | -8.2 | 2e-14 | 33/45 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.657×** | -7.7 | 8e-13 | 42/48 (SNU-423, HOP62, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.702×** | -6.5 | 5e-09 | 41/48 (HEC-1-A, SW1417, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.695×** | -6.4 | 7e-09 | 31/48 (C32, NCI-H1573, …) | rises with dose | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.537×** | -5.7 | 6e-07 | 42/48 (MIA PaCa-2, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.916× | -5.6 | 1e-06 | 0/50 | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.749×** | -5.3 | 4e-06 | 37/48 (C32, LoVo, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **0.752×** | -5.2 | 7e-06 | 31/48 (RPMI-7951, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.834× | -4.7 | 9e-05 | 20/48 (HOP62, SNU-423, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.642×** | -4.1 | 0.002 | 30/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.670×** | -3.7 | 0.006 | 26/48 (HEC-1-A, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.686×** | -3.5 | 0.014 | 26/48 (HEC-1-A, SW 1271, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.700×** | -3.3 | 0.026 | 23/47 (RKO, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.755×** | -3.0 | 0.065 | 19/48 (LOX-IMVI, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.724×** | -3.0 | 0.067 | 23/48 (SW1417, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.853× | -2.9 | 0.074 | 21/48 (C32, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8042. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 172 | 0 | 12 (9 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.123× (z -23.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.248× (z -23.0) |
| [[HOP62 (line)]] | alt | 160 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -22.3) |
| [[MIA PaCa-2 (line)]] | alt | 149 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.231× (z -17.6) |
| [[NCI-H1573 (line)]] | alt | 217 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -34.3) |
| [[A549 (line)]] | wt | 193 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.355× (z -13.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.594× (z -9.5) |
| [[SNU-423 (line)]] | alt | 162 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -26.9) |
| [[A-172 (line)]] | wt | 143 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -23.9) |
| [[LOX-IMVI (line)]] | wt | 223 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.330× (z -13.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.545× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 153 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -16.5) |
| [[SK-MEL-2 (line)]] | alt | 108 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -21.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.311× (z -16.2) |
| [[HepG2_C3A (line)]] | wt | 128 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.300× (z -11.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H23 (line)]] | alt | 86.7 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.359× (z -15.6) |
| [[NCI-H2347 (line)]] | alt | 265 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.365× (z -12.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.578× (z -9.2) |
| [[SW480 (line)]] | alt | 111 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.429× (z -12.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[AsPC-1 (line)]] | alt | 215 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.415× (z -10.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HEC-1-A (line)]] | alt | 120 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.411× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.506× (z -9.2) |
| [[KATO III (line)]] | alt | 96.9 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.451× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[LoVo (line)]] | wt | 186 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.521× (z -8.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 144 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.370× (z -11.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 154 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -12.7) |
| [[Panc 03.27 (line)]] | alt | 162 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.548× (z -10.1) |
| [[PANC-1 (line)]] | alt | 132 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.536× (z -9.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[CFPAC-1 (line)]] | alt | 155 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -13.9) |
| [[HS-578T (line)]] | alt | 103 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -12.7) |
| [[RPMI-7951 (line)]] | alt | 92.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -10.3) |
| [[A-427 (line)]] | wt | 151 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.406× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[C-33 A (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[COLO 205 (line)]] | alt | 104 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +9.3) | — |
| [[H4 (line)]] | wt | 92.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -11.5) |
| [[hTERT-HPNE (line)]] | wt | 127 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -11.8) |
| [[J82 (line)]] | alt | 102 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -14.2) |
| [[LS 180 (line)]] | wt | 145 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.446× (z -9.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 151 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.408× (z -9.1) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 120 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -10.4) |
| [[SW1417 (line)]] | alt | 76.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.467× (z -9.7) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 109 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -10.9) |
| [[A498 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 172 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 88.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 94.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 177 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8042), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP22]] | +0.63 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[BRD3]] | +0.59 | +0.36 / +0.61 | both halves | 9e-05 |  |
| [[BRWD1]] | +0.57 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[FBXL20]] | +0.56 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[HERPUD2]] | +0.56 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[CNIH4]] | +0.55 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[GPBP1L1]] | +0.54 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[ORMDL1]] | +0.54 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[HSDL2]] | +0.54 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[FGFR1OP2]] | +0.53 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[EZH1]] | +0.53 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[ZBTB44]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF628]] | -0.56 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[TRIM16]] | -0.55 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[XKR6]] | -0.50 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ZSCAN5A]] | -0.50 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[EGF]] | -0.50 | -0.53 / -0.46 | both halves | 3e-05 | pathway: Cargo recognition for clathrin-mediated endocytosis |
| [[EDC3]] | -0.50 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[ZBTB17]] | -0.49 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[SLC35A4]] | -0.48 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[RTL6]] | -0.48 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[GCNT2]] | -0.47 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[DRG2]] | -0.47 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[LMCD1-AS1]] | -0.47 | -0.49 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 234]]; 5 genes; every member is in the + arm (projection on the module's main direction 0.759). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (1.9, -41.5); signed map (-16.5, 13.0). **Vector** length 104, 35.2% of its response variance represented; |z| ≥ 3 in 1,229 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.2 | -0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.0 | +0.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.2 | +0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.4 | +0.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.4 | +1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.7 | -13.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.8 | -8.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.3 | -6.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.0 | -5.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.7 | -6.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.7 | -3.7 |
|  | [[EX229 (drug)]] 5 µM |  | -3.6 | -3.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.6 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -7.7 |

## What is on record

|  |  |
|---|---|
| Name | FCH and mu domain containing endocytic adaptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:72,956,041-73,090,522 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | F-BAR domain containing |
| Reactome | 4 pathways, smallest: Cargo recognition for clathrin-mediated endocytosis; Clathrin-mediated endocytosis; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q0JRZ9](https://www.uniprot.org/uniprotkb/Q0JRZ9) (F-BAR domain only protein 2):

> Functions in an early step of clathrin-mediated endocytosis. Has both a membrane binding/bending activity and the ability to recruit proteins essential to the formation of functional clathrin-coated pits. Has a lipid-binding activity with a preference for membranes enriched in phosphatidylserine and phosphoinositides (Pi(4,5) biphosphate) like the plasma membrane. Its membrane-bending activity might be important for the subsequent action of clathrin and adaptors in the formation of …

**Summary**, from NCBI Gene [115548](https://www.ncbi.nlm.nih.gov/gene/115548):

> Enables identical protein binding activity. Involved in clathrin coat assembly and clathrin-dependent endocytosis. Located in clathrin-coated pit and clathrin-coated vesicle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25180](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25180) · Entrez [115548](https://www.ncbi.nlm.nih.gov/gene/115548) · UniProt [Q0JRZ9](https://www.uniprot.org/uniprotkb/Q0JRZ9) · Ensembl [ENSG00000157107](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157107)

## Data

Gene col 8042: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8042); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8042, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8042]; `tensor/DDL_lfc|DDL_z.npy` [8042]; `embed/gene_vectors.npy` [8042]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8042 or target_col == 8042). Every well: [[FCHO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FCHO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
