---
symbol: "BLTP2"
type: "gene"
col: 139
ensembl_id: "ENSG00000007202"
name: "bridge-like lipid transfer protein family member 2"
location: "17q11.2"
module: 50
arm: "+"
pooled_cpm: 95.82
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# BLTP2

*bridge-like lipid transfer protein family member 2* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.23× (z +14.4, q 4e-44, up in 36 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.74× (z +11.1, q 4e-26, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.514× (z -18.8, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCNX3]] (+0.76, fdr 7e-06), [[SLC25A39]] (+0.72, fdr 7e-06), [[CHID1]] (+0.71, fdr 7e-06); moves opposite to [[ZMYM5]] (-0.71, fdr 7e-06), [[ABCA5]] (-0.69, fdr 7e-06), [[TERF2IP]] (-0.68, fdr 7e-06).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[IRAG2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 139.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.23×** | +14.4 | 4e-44 | 36/50 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.78×** | +11.5 | 6e-28 | 40/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.74×** | +11.1 | 4e-26 | 40/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +10.5 | 9e-24 | 40/48 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.39×** | +6.6 | 6e-09 | 32/49 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.30×** | +5.0 | 7e-05 | 23/44 (SW480, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +4.8 | 1e-04 | 27/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.26×** | +4.6 | 3e-04 | 26/48 (A549, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.24×** | +4.3 | 0.001 | 22/48 (COLO 205, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Rimonabant (Hydrochloride) (drug)]] 0.05 µM | ⚠ unreliable plate only; position correction uncertain | **1.23×** | +4.1 | 0.003 | 26/49 (SW 900, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.006 | 22/49 (COLO 205, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.24×** | +3.7 | 0.010 | 22/45 (SW480, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.20× | +3.6 | 0.015 | 17/48 (RKO, KATO III, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.19× | +3.5 | 0.022 | 16/48 (KATO III, SW480, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.046 | 21/48 (KATO III, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pentagastrin (drug)]] 5 µM |  | 1.12× | +3.2 | 0.046 | 1/48 (NCI-H1792) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 139.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.514×** | -18.8 | 0e+00 | 43/48 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.501×** | -13.3 | 8e-38 | 46/48 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.546×** | -12.1 | 2e-31 | 37/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.630×** | -9.2 | 4e-18 | 40/48 (BT-474, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.727×** | -6.4 | 2e-08 | 34/48 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.757×** | -5.6 | 2e-06 | 31/48 (BT-474, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.787×** | -4.8 | 1e-04 | 30/49 (Panc 03.27, HS-578T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.792×** | -4.7 | 2e-04 | 26/48 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.824×** | -3.9 | 0.006 | 22/48 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | 0.847× | -3.2 | 0.076 | 17/49 (HS-578T, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 139. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 112 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -18.2) |
| [[A-172 (line)]] | wt | 95.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -27.6) |
| [[A549 (line)]] | wt | 89.5 | 2 (1 ⚠) | 3 | [[Panobinostat (drug)]] 5 µM 2.05× (z +8.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.03× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -17.1) |
| [[NCI-H1573 (line)]] | alt | 77.1 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.199× (z -17.4) |
| [[SNU-423 (line)]] | alt | 54.6 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -10.3) |
| [[C32 (line)]] | wt | 75.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -17.1) |
| [[HEC-1-A (line)]] | alt | 120 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -20.0) |
| [[NCI-H2347 (line)]] | alt | 77.6 | 3 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.02× (z +9.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.01× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.631× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 170 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -12.2) |
| [[SNU-1 (line)]] | wt | 113 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -14.5) |
| [[SW480 (line)]] | alt | 82.8 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.54× (z +13.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.15× (z +10.8) | — |
| [[C-33 A (line)]] | alt | 161 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 34.0 | 3 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.01× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 70.9 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.95× (z +9.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.82× (z +9.1) | — |
| [[J82 (line)]] | alt | 103 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -23.4) |
| [[LoVo (line)]] | wt | 83.2 | 2 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.36× (z +11.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 1.93× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 163 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -17.1) |
| [[Panc 03.27 (line)]] | alt | 92.1 | 2 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.41× (z +11.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.05× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -12.1) |
| [[PANC-1 (line)]] | alt | 133 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -20.7) |
| [[A-427 (line)]] | wt | 110 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -35.2) |
| [[A498 (line)]] | wt | 106 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -12.8) |
| [[HOP62 (line)]] | alt | 71.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -10.5) |
| [[Hs 766T (line)]] | wt | 52.0 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.51× (z +8.6) ⚠ cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -11.1) |
| [[HT-29 (line)]] | alt | 84.0 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.30× (z +8.8) ⚠ cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -9.3) |
| [[KATO III (line)]] | alt | 95.5 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.38× (z +9.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.13× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 84.0 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.22× (z +8.9) ⚠ cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 94.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.27× (z +8.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 65.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H2030 (line)]] | alt | 171 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -15.7) |
| [[SK-MEL-2 (line)]] | alt | 82.8 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.248× (z -14.1) |
| [[SW 900 (line)]] | alt | 51.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.344× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.346× (z -10.3) |
| [[AN3 CA (line)]] | alt | 97.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.128× (z -13.0) |
| [[AsPC-1 (line)]] | alt | 52.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -12.6) |
| [[HS-578T (line)]] | alt | 86.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -10.9) |
| [[NCI-H596 (line)]] | alt | 82.9 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.148× (z -9.7) |
| [[RKO (line)]] | wt | 114 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.407× (z -9.3) |
| [[SHP-77 (line)]] | alt | 98.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.378× (z -10.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 97.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -11.4) |
| [[SW48 (line)]] | wt | 102 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -13.5) |
| [[CHP-212 (line)]] | wt | 65.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 57.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 62.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 104 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 105 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 139), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNX3]] | +0.76 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[SLC25A39]] | +0.72 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[CHID1]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[NIPA2]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[RNPS1]] | +0.70 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[NOMO3]] | +0.70 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[FBXW2]] | +0.69 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[TBC1D24]] | +0.68 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[COLGALT1]] | +0.68 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[APMAP]] | +0.68 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[RPE]] | +0.68 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[PRKDC]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM5]] | -0.71 | -0.71 / -0.68 | both halves | 7e-06 |  |
| [[ABCA5]] | -0.69 | -0.69 / -0.62 | both halves | 7e-06 |  |
| [[TERF2IP]] | -0.68 | -0.71 / -0.61 | both halves | 7e-06 |  |
| [[WBP4]] | -0.67 | -0.68 / -0.56 | both halves | 1e-05 |  |
| [[ZNF226]] | -0.67 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[UNK]] | -0.67 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[EIF4EBP3]] | -0.66 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[N4BP2L1]] | -0.65 | -0.66 / -0.58 | both halves | 8e-06 |  |
| [[LRCH3]] | -0.65 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[STAP2]] | -0.65 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[TMEM265]] | -0.64 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[SMDT1]] | -0.64 | -0.73 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRAG2]] | B | IRAG2 activity lowers BLTP2's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 1.39× higher at baseline in the lines without IRAG2 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.594). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.6, -26.3); signed map (-26.9, -42.4). **Vector** length 139, 42.9% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +7.0 | +11.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.5 | +11.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.5 | +10.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.8 | +4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +3.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.4 | +3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Isocorydine (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -11.9 | -18.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.9 | -13.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.5 | -12.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.3 | -9.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -5.5 | -4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.4 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -2.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -4.0 | -2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.6 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | bridge-like lipid transfer protein family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,614,446-28,645,454 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686M0843, MGC111488, BCOX1, CT101, BCOX, FMP27, Hob; previously KIAA0100 |
| Gene groups (HGNC) | Bridge-like lipid transfer protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14667](https://www.uniprot.org/uniprotkb/Q14667) (Bridge-like lipid transfer protein family member 2):

> Tube-forming lipid transport protein which binds to phosphatidylinositols and affects phosphatidylinositol-4,5-bisphosphate (PtdIns-4,5-P2) distribution.

**Summary**, from NCBI Gene [9703](https://www.ncbi.nlm.nih.gov/gene/9703):

> This gene was initially characterized in human as having high expression levels in breast carcinomas and breast cancer cell lines. This gene also has increased expression in prostrate cancer cells relative to normal prostrate tissues. Expression of this gene is negatively regulated by direct binding of the microRNA miR-195 to its 3' UTR. miR-195 has been shown to modulate the invasiveness of prostrate cancer cells and xenograft metastases by downgrading expression of this gene. In mouse, the …

**Accessions** — [HGNC:28960](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28960) · Entrez [9703](https://www.ncbi.nlm.nih.gov/gene/9703) · UniProt [Q14667](https://www.uniprot.org/uniprotkb/Q14667) · Ensembl [ENSG00000007202](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000007202)

## Data

Gene col 139: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 139); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 139, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 139]; `tensor/DDL_lfc|DDL_z.npy` [139]; `embed/gene_vectors.npy` [139]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 139 or target_col == 139). Every well: [[BLTP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BLTP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
